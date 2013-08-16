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

    def __str_clean__(self, depth=0):
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
    def isLeft(self, key=lambda k: k):
        """Is element left child of its parent or not"""
        if self.parent is None:
            return None
        return key(self.value) < key(self.parent.value)

    def isRight(self, key=lambda k: k):
        return not self.isLeft(self, key=key)

    def hasOneChild(self):
        """If element has exactly one child"""
        return (self.l_child is not None and self.r_child is None) or (
        self.r_child is not None and self.l_child is None)

    def get_one_child(self):
        """Get one child of element (uses with hasOneChild)"""
        if self.l_child is not None:
            return self.l_child
        return self.r_child

    def min(self):
        """Return element with min key"""
        min_element = self
        while min_element.l_child is not None:
            min_element = min_element.l_child
        return min_element

    def max(self):
        """Return element with max key"""
        max_element = self
        while max_element.r_child is not None:
            max_element = max_element.r_child
        return max_element

    def successor(self, key = lambda k:k):
        """Return next element with greater key or None"""
        if self.r_child is not None:
            return self.r_child.min()
        parent = self.parent
        # note: not None == True
        while not parent.isLeft(key) and parent.isLeft(key) is not None:
            parent = parent.parent
        return parent

    def search(self, key_value, key=lambda k:k):
        """Return element with key_value"""
        elem = self
        while elem is not None and key_value != key(elem.value):
            if key_value < key(elem.value):
                elem = elem.l_child
            else:
                elem = elem.r_child
        return elem

    def insert(self, element, key=lambda k: k):
        """Insert element into correct place in tree"""
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

    def delete(self, key=lambda k: k):
        """Delete element and return root of the tree."""

        if self.isLeaf():
            if self.isRoot():
                self.value = None
            elif self.isLeft(key):
                self.parent.l_child = None
            else:
                self.parent.r_child = None
            return self.get_root()

        if self.hasOneChild():
            ch = self.get_one_child()
            ch.parent = self.parent
            if self.isRoot():
                pass
            elif self.isLeft(key):
                self.parent.l_child = ch
            else:
                self.parent.r_child = ch
            return ch.get_root()

        # if self.hasTwoChildren():
        # this element always is the left in right subtree
        new_element_in_pos = self.r_child.min()
        # remove our replacing element from its current position
        if new_element_in_pos.isLeft(key):
            new_element_in_pos.parent.l_child = new_element_in_pos.r_child
        else:
            new_element_in_pos.parent.r_child = new_element_in_pos.r_child
        if new_element_in_pos.r_child is not None:
            new_element_in_pos.r_child.parent = new_element_in_pos.parent
        # make new element learn his place
        new_element_in_pos.parent = self.parent
        new_element_in_pos.l_child = self.l_child
        new_element_in_pos.r_child = self.r_child
        # make parent and children of our new element learn his place
        if self.isRoot():
            pass
        elif self.isLeft(key):
            self.parent.l_child = new_element_in_pos
        else:
            self.parent.r_child = new_element_in_pos
        if self.l_child is not None:
            self.l_child.parent = new_element_in_pos
        if self.r_child is not None:
            self.r_child.parent = new_element_in_pos
        return new_element_in_pos.get_root()



