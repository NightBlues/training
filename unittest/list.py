# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from datastruct.list import *

element = LinkedList('hi')
element2 = element.set_next(LinkedList('there'))
element3 = element2.set_next(LinkedList('!'))
element4 = element3.set_next(LinkedList())
element5 = element4.set_next(LinkedList('elem5'))
element6 = element5.set_next(LinkedList('elemental'))
element7 = element6.set_next(LinkedList('element7'))

el = element
while el:
    print(el)
    el = el.nextEl
print
el = element7
while el:
    print(el)
    el = el.prevEl


stack1 = Stack()
for n in range(7):
    stack1.push('instance ' + str(n))
print(stack1)
while not stack1.isEmpty():
    print((stack1.pop()))
stack1.flush()
print(stack1)
