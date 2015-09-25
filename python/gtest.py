from __future__ import print_function
import gevent
import random
import time

# def task(pid):
# 	"""
# 	Some non-deterministic task
# 	"""
# 	gevent.sleep(random.randint(0, 2) * 0.001)
# 	print('Task %s done' % pid)

# def synchronous():
# 	for i in range(1, 10):
# 		task(i)

# def asynchronous():
# 	threads = [gevent.spawn(task, i) for i in xrange(10)]
# 	gevent.sleep(10)
# 	# gevent.joinall(threads)

# print('Synchronous:')
# synchronous()

# print('Asynchronous:')
# asynchronous()

def task(pid, sleep=1):
	gevent.sleep(sleep)
	for i in range(100):
		print("from pid {0}".format(pid))
		gevent.sleep(sleep)

tasks = [
	gevent.spawn(task, "worker1", sleep=1.5),
	gevent.spawn(task, "worker2"),
	gevent.spawn(task, "worker3")
]

gevent.joinall(tasks)
