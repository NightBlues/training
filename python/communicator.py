import sys

data = 'helo' * 64
for i in range(10):
    sys.stdout.write(data + '\n')
    sys.stdout.flush()
    data = sys.stdin.read(64)
    sys.stderr.write('iteration {}\n'.format(i))
    sys.stderr.flush()
# sys.stdout.close()
# sys.stderr.close()
