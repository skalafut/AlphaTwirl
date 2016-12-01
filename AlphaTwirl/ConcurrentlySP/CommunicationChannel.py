# Tai Sakuma <tai.sakuma@cern.ch>
import os
import shutil
import subprocess
import pickle
import datetime
import tempfile
import collections
from operator import itemgetter

from ..ProgressBar import NullProgressMonitor
from ..mkdir_p import mkdir_p

##__________________________________________________________________||
TaskPackage = collections.namedtuple(
    'TaskPackage',
    'index task progressReporter args kwargs'
)

##__________________________________________________________________||
class TaskDirectory(object):
    def __init__(self, path):

        # create a task directory
        prefix = 'tpd_{:%Y%m%d_%H%M%S}_'.format(datetime.datetime.now())
        # e.g., 'tpd_20161129_122841_'

        self.taskdir = tempfile.mkdtemp(prefix = prefix, dir = path)
        # e.g., '{path}/tpd_20161129_122841_HnpcmF'

        # copy run.py to the task dir
        thisdir = os.path.dirname(__file__)
        src = os.path.join(thisdir, 'run.py')
        shutil.copy(src, self.taskdir)

##__________________________________________________________________||
class CommunicationChannel(object):
    """An implementation of concurrency with subprocess.

    """
    def __init__(self, progressMonitor = None, tmpdir = '_ccsp_temp'):
        self.progressMonitor = NullProgressMonitor() if progressMonitor is None else progressMonitor
        self.results = [ ]
        self.tmpdir = tmpdir
        self.running_task_idxs = collections.deque()
        self.running_procs = collections.deque()

    def begin(self):
        self.progressReporter = self.progressMonitor.createReporter()

        mkdir_p(self.tmpdir)

        self.taskDirectory = TaskDirectory(path = self.tmpdir)

        self.task_idx = -1 # so it starts from 0

    def put(self, task, *args, **kwargs):
        self.task_idx += 1
        package = TaskPackage(self.task_idx, task, self.progressReporter, args, kwargs)
        basename = 'task_{:05d}.p'.format(self.task_idx)
        path = os.path.join(self.taskDirectory.taskdir, basename)
        f = open(path, 'wb')
        pickle.dump(package, f)
        proc = self._run(self.task_idx)
        self.running_task_idxs.append(self.task_idx)
        self.running_procs.append(proc)

    def _run(self, task_idx):
        run_script = os.path.join(self.taskDirectory.taskdir, 'run.py')
        basename = 'task_{:05d}.p'.format(task_idx)
        path = os.path.join(self.taskDirectory.taskdir, basename)
        args = [run_script, path]
        proc = subprocess.Popen(args, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        return proc

    def receive(self):
        while self.running_procs:
            proc = self.running_procs.popleft()
            proc.communicate()

        task_idx_result_pairs = [ ]
        while self.running_task_idxs:
            task_idx = self.running_task_idxs.popleft()
            dirname = 'task_{:05d}'.format(task_idx)
            path = os.path.join(self.taskDirectory.taskdir, 'results', dirname, 'result.p')
            f = open(path, 'rb')
            result = pickle.load(f)
            task_idx_result_pairs.append((task_idx, result))

        task_idx_result_pairs = sorted(task_idx_result_pairs, key = itemgetter(0))

        results = [result for idx, result in task_idx_result_pairs]
        return results

    def end(self):
        del self.taskDirectory.taskdir
        del self.task_idx

##__________________________________________________________________||
