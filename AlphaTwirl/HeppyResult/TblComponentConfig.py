# Tai Sakuma <tai.sakuma@cern.ch>
from ..misc import mkdir_p
from ..misc import listToAlignedText
import os

##__________________________________________________________________||
class TblComponentConfig(object):
    def __init__(self, outPath, columnNames, keys):
        self._outPath = outPath
        self.columnNames = columnNames
        self._rows = [['component'] + list(columnNames)]
        self._keys = keys

    def begin(self): pass

    def read(self, component):

        cfg = component.config()
        if cfg is None: return
        if not all([k in cfg for k in self._keys]): return

        vals =  [cfg[k] for k in self._keys]
        self._rows.append([component.name] + vals)

    def end(self):
        if len(self._rows) == 1: return

        f = self._open(self._outPath)
        f.write(listToAlignedText(self._rows))
        self._close(f)

    def _open(self, path):
        mkdir_p(os.path.dirname(path))
        return open(path, 'w')

    def _close(self, file): file.close()

##__________________________________________________________________||
