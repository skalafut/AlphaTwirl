# Tai Sakuma <sakuma@fnal.gov>
import multiprocessing

##____________________________________________________________________________||
class Worker(multiprocessing.Process):
    def __init__(self, task_queue, result_queue, lock):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.lock = lock

    def run(self):
        while True:
            task = self.task_queue.get()
            if task is None:
                self.task_queue.task_done()
                break
            readers = task()
            self.task_queue.task_done()
            self.result_queue.put(readers)

##____________________________________________________________________________||
class Task(object):
    def __init__(self, eventBuilder, component, readers):
        self.eventBuilder = eventBuilder
        self.component = component
        self.readers = readers

    def __call__(self):
        events = self.eventBuilder.build(self.component)
        for event in events:
            for reader in self.readers:
                reader.event(event)
        return self.readers

##____________________________________________________________________________||
class EventLooperMP(object):
    def __init__(self, nprocesses = 16):
        self._nprocesses = nprocesses
        self._allReaders = { }
        self._tasks = multiprocessing.JoinableQueue()
        self._results = multiprocessing.Queue()
        self._ntasks = 0
        self._lock = multiprocessing.Lock()
        for i in xrange(self._nprocesses):
            worker = Worker(self._tasks, self._results, self._lock)
            worker.start()

    def read(self, eventBuilder, component, readers):
        # add ids so can collect later
        for reader in readers:
            reader.id = id(reader)
            self._allReaders[id(reader)] = reader

        task = Task(eventBuilder, component, readers)
        self._tasks.put(task)
        self._ntasks += 1

    def end(self):
        # end processes
        for i in xrange(self._nprocesses):
            self._tasks.put(None)
        self._tasks.join()

        # collect readers from processes
        for i in xrange(self._ntasks):
            readers = self._results.get()
            for reader in readers:
                self._allReaders[reader.id].setResults(reader.results())

##____________________________________________________________________________||
class EventReaderBundleMP(object):

    def __init__(self, eventBuilder, nprocesses = 16):
        self._eventBuilder = eventBuilder
        self._packages = [ ]
        self._nprocesses = nprocesses

    def addReaderPackage(self, package):
        self._packages.append(package)

    def begin(self):
        self._eventLooper = EventLooperMP(self._nprocesses)

    def read(self, component):
        readers = [package.make(component.name) for package in self._packages]
        self._eventLooper.read(self._eventBuilder, component, readers)

    def end(self):
        self._eventLooper.end()

        for package in self._packages:
            package.collect()

##____________________________________________________________________________||