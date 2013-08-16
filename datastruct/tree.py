__author__ = 'nightblues'


class BinaryTree():
    def __init__(self, value=None):
        self.parent = None
        self.l_child = None
        self.r_child = None
        self.value = value

    def set_left_child(self, el):
        if not isinstance(el, self.__class__):
            el = self.__class__(el)
        self.l_child = el
        el.parent = self

    def set_right_child(self, el):
        if not isinstance(el, self.__class__):
            el = self.__class__(el)
        self.r_child = el
        el.parent = self

    def get_root(self):
        root = self
        while root.parent is not None:
            root = root.parent
        return root

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self.l_child is None and self.r_child is None

    def isEmpty(self):
        return self.isLeaf() and self.isRoot() and self.value is None

    def bfs(self):
        """breadth-first search"""
        heap = []
        heap.append(self)
        while len(heap) > 0:
            if heap[0].l_child is not None:
                heap.append(heap[0].l_child)
            if heap[0].r_child is not None:
                heap.append(heap[0].r_child)
            yield heap.pop(0)

    def print_tree(self):
        print(self.get_root().__str_clean__())

    def __str_clean__(self, depth = 0):
        left = "\t" * (depth + 1) + str(None) + "\n"
        right = "\t" * (depth + 1) + str(None) + "\n"
        if isinstance(self.l_child, self.__class__):
            left = self.l_child.__str_clean__(depth=depth + 1)
        if isinstance(self.r_child, self.__class__):
            right = self.r_child.__str_clean__(depth=depth + 1)
        result = "\t" * depth + str(self.value) + "\n"
        if not self.isLeaf():
            result += str(left)
            result += str(right)
        return result

    def __unicode__(self):
        str_position = ""
        if self.isRoot():
            str_position = "root"
        elif self.isLeaf():
            str_position = "leaf"
        else:
            str_position = "regular"
        return "<%s element, \"%s\" (%s)>" % (self.__class__.__name__, self.value, str_position)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class BinarySearchTree(BinaryTree):
    def insert(self, element, key=lambda k: k):
        if not isinstance(element, self.__class__):
            element = self.__class__(element)
        el_parent_place = None
        el_place = self.get_root()
        if el_place.isEmpty():
            el_place.value = element.value
            return
        while el_place is not None:
            el_parent_place = el_place
            if key(element.value) < key(el_place.value):
                el_place = el_place.l_child
            else:
                el_place = el_place.r_child
        element.parent = el_parent_place
        if element.isRoot():
            return
        if key(element.value) < key(element.parent.value):
            element.parent.set_left_child(element)
        else:
            element.parent.set_right_child(element)

    # def delete(self):
