__author__ = 'nightblues'


class LinkedList(object):
    def __init__(self, value=None):
        self.value = value
        self.nextEl = None
        self.prevEl = None

    def get_tail(self):
        """Return last element (tail)"""
        tail = self
        while tail.nextEl is not None:
            tail = tail.nextEl
        return tail

    def get_head(self):
        """Return first element (head)"""
        head = self
        while head.prevEl is not None:
            head = head.prevEl
        return head

    def insert(self, el):
        """Insert element before current(self)"""
        if not isinstance(el, self.__class__):
            el = self.__class__(el)
        el.prevEl, el.nextEl = self.prevEl, self
        self.prevEl.nextEl = el
        self.prevEl = el

    def append(self, el):
        if not isinstance(el, self.__class__):
            el = self.__class__(el)
        tail = self.get_tail()
        el.prevEl = tail
        tail.nextEl = el

    def delete(self):
        if not self.isHead():
            self.prevEl.nextEl = self.nextEl
        if not self.isTail():
            self.nextEl.prevEl = self.prevEl

    def search(self, value):
        head = self.get_head()
        for el in head:
            if el.value == value:
                return el

    def next(self):
        return self.nextEl

    def prev(self):
        return self.prevEl

    def isHead(self):
        return self.prevEl is None

    def isTail(self):
        return self.nextEl is None

    def __iter__(self):
        return LinkedListIterator(self)

    def __unicode__(self):
        str_position = ""
        if self.isHead():
            str_position = "head"
        elif self.isTail():
            str_position = "tail"
        else:
            str_position = "regular"
        return "<LinkedList element, \"%s\" (%s)>" % (self.value, str_position)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class LinkedListIterator():
    def __init__(self, startEl):
        self.currentEl = startEl

    def __next__(self):
        if self.currentEl is None:
            raise StopIteration
        cur = self.currentEl
        if self.currentEl.isTail():
            self.currentEl = None
        else:
            self.currentEl = self.currentEl.nextEl
        return cur

    