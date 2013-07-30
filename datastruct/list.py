# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from datastruct import heap

class LinkedList(object):

    def __init__(self, value=None):
        self.value = value
        self.nextEl = None
        self.prevEl = None

    def get_tail(self):
        """Return last element (tail)"""
        tail = self.nextEl
        while tail.nextEl is not None:
            tail = tail.nextEl
        return tail

    def get_head(self):
        """Return first element (head)"""
        head = self.prevEl
        while head.prevEl is not None:
            head = head.prevEl
        return head

    def insert(self, el):
        """Insert element before current(self)"""
        el.prevEl, el.nextEl = self.prevEl, self
        self.prevEl.nextEl = el
        self.prevEl=el

    def append(self, el):
        tail = self.get_tail()
        el.prevEl = tail
        tail.nextEl = el

    def delete(self):
        self.prevEl.nextEl = self.nextEl
        self.nextEl.prevEl = self.prevEl

    def search(self, value):
        pass

    def __unicode__(self):
        str_position = ""
        if self.prevEl is None:
            if self.nextEl is None:
                str_position = "only"
            else:
                str_position = "first"
        else:
            if self.nextEl is None:
                str_position = "last"
            else:
                str_position = "regular"
        return "<LinkedList element, \"%s\" (%s)>" % (self.value, str_position)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class Stack(object):

    def __init__(self):
        self.data = []

    def __unicode__(self):
        return "<Stack, elements: %d, last:\"%s\">" %\
         (len(self.data), self.top())

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def isEmpty(self):
        return (len(self.data) == 0)

    def flush(self):
        self.data = []

    def top(self):
        if self.isEmpty():
            return None
        return self.data[-1]

    def pop(self):
        if self.isEmpty():
            return None
        return self.data.pop()

    def push(self, el):
        """el - element of stack"""
        self.data.append(el)

class Queue():
    def __init__(self, length=10):
        self.length=length+1
        self.clear()

    def enqueue(self, el):
        if self.isFull():
            raise OverflowError
        self.tail = (self.tail + 1)%self.length
        self.data[self.tail] = el

    def dequeue(self):
        if self.isEmpty():
            return None
        self.head = (self.head + 1)%self.length
        element = self.data[self.head]
        self.data[self.head] = None
        return element

    def clear(self):
        self.head=0
        self.tail=0
        self.data = [None for i in range(self.length)]

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return (self.tail + 1)%self.length == self.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.isEmpty():
            raise StopIteration
        return self.dequeue()

    def __unicode__(self):
        return "<Queue, elements: (%d,%d) %s>" % (self.head,self.tail,self.data)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


# queue with priority
class PriorityQueue():

    def __init__(self, elements=None, comp=lambda a,b:a>b):
        self.comp=comp
        if elements is None:
            self.data = []
        else:
            self.data=elements
            self._make_heap()

    def _make_heap(self):
        for i in reversed(range(len(self.data)//2)):
            heap.pushdown(self.data,i, comp=self.comp)

    def isEmpty(self):
        return not len(self.data)>0

    def append(self, el):
        self.data.enqueue(el)
        heap.pushup(self.data, len(self.data)-1, self.comp)

    def pop(self):
        return heap.pop(self.data, comp=self.comp)

    def __iter__(self):
        return self

    def __next__(self):
        if self.isEmpty():
            raise StopIteration
        else:
            return self.pop()
