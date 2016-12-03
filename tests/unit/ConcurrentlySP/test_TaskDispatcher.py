import unittest
import os
import stat
import tempfile
import shutil

from AlphaTwirl.ConcurrentlySP import TaskDispatcher

##__________________________________________________________________||
run_py = """
#!/usr/bin/env python
import time
import sys
time.sleep(float(sys.argv[1]))
print ' '.join(sys.argv)
"""
run_py = run_py.lstrip()

##__________________________________________________________________||
class TestTaskDispatcher(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _copy_run_script_to_taskdir(self, content, taskdir):
        path = os.path.join(taskdir, 'run.py')
        f = open(path, 'w')
        f.write(content)
        f.close()
        os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR)

    def test_run_wait(self):
        self._copy_run_script_to_taskdir(run_py, self.tmpdir)
        obj = TaskDispatcher(pipe = True)
        obj.run(taskdir = self.tmpdir, package_path = '0.20')
        obj.run(taskdir = self.tmpdir, package_path = '0.02')
        obj.run(taskdir = self.tmpdir, package_path = '0.15')
        expected = [
            ('{}/run.py 0.20\n'.format(self.tmpdir), ''),
            ('{}/run.py 0.02\n'.format(self.tmpdir), ''),
            ('{}/run.py 0.15\n'.format(self.tmpdir), ''),
        ]
        actual = obj.wait()
        self.assertEqual(expected, actual)

##__________________________________________________________________||

