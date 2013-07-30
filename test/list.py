# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from datastruct.list import *
from test.util import CompEl

# stack1 = Stack()
# for n in range(7):
#     stack1.push('instance ' + str(n))
# print(stack1)
# while not stack1.isEmpty():
#     print((stack1.pop()))
# stack1.flush()
# print(stack1)


# elements = [CompEl("Hi",1),CompEl("there",2), CompEl("my",3),CompEl("name",4), CompEl("is",6), CompEl("Vadim",6)]
# queue = PriorityQueue(elements, comp=lambda a,b: a.key<=b.key)
# # while not queue.isEmpty():
# #     print(queue.pop())
# for e in queue:
#     print(e)

# queue = Queue(5)
# print(queue)
# for i in range(5):
#     queue.enqueue(CompEl(chr(97+i), i))
# print(queue)
# # while not queue.isEmpty():
# #     print(queue.pop())
# # print(queue)
# for e in queue:
#     print(e)
# print(queue)
# queue.enqueue(CompEl(chr(97+10), 10))
# print(queue)