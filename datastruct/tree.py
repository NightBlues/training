__author__ = 'nightblues'

class BinaryTree():

    def __init__(self, value = None):
        self.parent = None
        self.l_child = None
        self.r_child = None
        self.value = value

    def set_left_child(self, el):
        if not isinstance(el, self.__class__):
            el = self.__class__(el)
        self.l_child = el
        el.parent=self

    def set_right_child(self, el):
        if not isinstance(el, self.__class__):
            el = self.__class__(el)
        self.r_child = el
        el.parent=self

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self.l_child is None and self.r_child is None

    def bfs(self):
        """breadth-first search"""
        heap = []
        heap.append(self)
        while len(heap)>0:
            if heap[0].l_child is not None:
                heap.append(heap[0].l_child)
            if heap[0].r_child is not None:
                heap.append(heap[0].r_child)
            yield heap.pop(0)

    def __unicode__(self):
        str_position = ""
        if self.isRoot():
            str_position = "root"
        elif self.isLeaf():
            str_position = "leaf"
        else:
            str_position = "regular"
        return "<BinaryTree element, \"%s\" (%s)>" % (self.value, str_position)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()
