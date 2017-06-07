from zipfile import ZipFile
import os
from StringIO import StringIO
from functools import partial


def open_func(obj, *args):
    """If Python was Clojure we could just specify `open` for our class..."""
    if hasattr(obj, 'open'):
        return obj.open(*args)
    return open(obj, *args)


class Writer(StringIO):
    def __init__(self, write_func, buf=''):
        self.write_func = write_func
        StringIO.__init__(self, buf=buf)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self.write_func(self.getvalue())
        StringIO.close(self)


class ZipPath(object):
    _file = None

    def __init__(self, filename, inner_path=''):
        self.filename = filename
        self.inner_path = inner_path

    def endswith(self, string):
        return self.inner_path.endswith(string)

    def startswith(self, string):
        return self.inner_path.startswith(string)

    def __add__(self, other):
        """Let os.path.join us with pathes."""
        other_path = other
        if isinstance(other, self.__class__):
            other_path = other.inner_path
        if self.inner_path == '' and other_path.startswith('/'):
            other_path = other_path[1:]
        return self.__class__(
            self.filename, os.path.join(self.inner_path, other_path))

    def open(self, mode='r', buffering=0):
        if self._file and self._file.mode != mode:
            self._file.close()
        if 'w' in mode:
            mode = 'a'
            def writer_func(data):
                
                self._file.writestr(self.inner_path, data)
        else:
            writer_func = partial(self._file.writestr, self.inner_path)
        self._file = ZipFile(self.filename, mode=mode)
        if 'a' in mode:
            self._file
            return Writer(writer_func)
        return self._file.open(self.inner_path, mode=mode)


path = ZipPath("/tmp/test.zip")
path = os.path.join(path, "hello.txt")

with open_func(path, "w") as fp:
    fp.write("hello!\n")


path = os.path.join(path, "secondfile.txt")
   
with open_func(path, "w") as fp:
    fp.write("This is content of the second file!\nSecond line!\n")
