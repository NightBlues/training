# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from datastruct.list import *
from test.util import CompEl

# element = LinkedList('hi')
# element2 = element.set_next(LinkedList('there'))
# element3 = element2.set_next(LinkedList('!'))
# element4 = element3.set_next(LinkedList())
# element5 = element4.set_next(LinkedList('elem5'))
# element6 = element5.set_next(LinkedList('elemental'))
# element7 = element6.set_next(LinkedList('element7'))
#
# el = element
# while el:
#     print(el)
#     el = el.nextEl
# print
# el = element7
# while el:
#     print(el)
#     el = el.prevEl
#
#
# stack1 = Stack()
# for n in range(7):
#     stack1.push('instance ' + str(n))
# print(stack1)
# while not stack1.isEmpty():
#     print((stack1.pop()))
# stack1.flush()
# print(stack1)



elements = [CompEl("Hi",1),CompEl("there",2), CompEl("my",3),CompEl("name",4), CompEl("is",6), CompEl("Vadim",6)]
queue = PriorityQueue(elements, comp=lambda a,b: a.key<=b.key)
# while not queue.isEmpty():
#     print(queue.pop())
for e in queue:
    print(e)
