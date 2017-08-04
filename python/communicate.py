import os
import fcntl
import select

from subprocess import Popen, PIPE
from StringIO import StringIO


class Popen_(Popen):
    def streaming_communicate(self, chunk_size=64):
        fin, fout = [self.stdin.fileno()], [self.stdout.fileno(),
                                            self.stderr.fileno()]
        for fd in fin + fout:
            fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)

        data = ''
        while True:
            out = None
            err = None
            rl, wl, _ = select.select(fout, fin, [], 3)
            if wl and data:
                writen = os.write(wl[0], data)
                data = data[writen:]
            for fd in rl:
                if fd == self.stdout.fileno():
                    out = os.read(fd, chunk_size)
                if fd == self.stderr.fileno():
                    err = os.read(fd, chunk_size)
            new_data = yield out, err
            if new_data is None:
                fin[:] = []
            else:
                data = data + new_data
            if self.poll() is not None:
                break

    def communicate(self, data, chunk_size=64):
        fin, fout = [self.stdin.fileno()], [self.stdout.fileno(),
                                            self.stderr.fileno()]
        for fd in fin + fout:
            fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)

        data_len = len(data)
        out, err = [], []
        offset = 0
        while True:
            rl, wl, _ = select.select(fout, fin, [], 3)
            if wl:
                stop = min(offset + chunk_size, data_len)
                chunk = data[offset:stop]
                writen = os.write(wl[0], chunk)
                offset += writen
                if offset == len(data):
                    self.stdin.close()
                    fin.pop()
            for fd in rl:
                if fd == self.stdout.fileno():
                    out.append(os.read(fd, chunk_size))
                if fd == self.stderr.fileno():
                    err.append(os.read(fd, chunk_size))
            if self.poll() is not None:
                break

        return ''.join(out), ''.join(err)


def process_data(data):
    p = Popen_(['python', 'communicator.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(data)
    print out, err


def process_data_streaming(input_, chunk_size=64):
    p = Popen_(['python', 'communicator.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    com = p.streaming_communicate(chunk_size=chunk_size)

    def __send_and_print(chunk):
        if chunk:
            out, err = com.send(chunk)
        else:
            out, err = next(com)
        if out is not None:
            print 'stdout: ', out
        if err is not None:
            print 'stderr: ', err
    __send_and_print(None)
    while True:
        chunk = input_.read(chunk_size)
        try:
            __send_and_print(chunk)
        except StopIteration:
            break


# process_data('a' * 512)
data = StringIO('b' * 1024)
process_data_streaming(data)
