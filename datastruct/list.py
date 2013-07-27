# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from datastruct import heap

class LinkedList(object):

    def __init__(self, value=None):
        self.value = value
        self.nextEl = None
        self.prevEl = None

    def set_next(self, el):
        """
        el - object of LinkedList class
        """
        self.nextEl = el
        el.prevEl = self
        return el

    def set_prev(self, el):
        """
        el - object of LinkedList class
        """
        self.nextEl = self
        el.prevEl = el
        return el

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
        self.data.append(el)
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
