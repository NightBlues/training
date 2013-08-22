__author__ = 'nightblues'
import sys
sys.path.append('..')
from datastruct.tree import *
from test.util import CompEl

# bt = BinaryTree()
# el = bt
# for i in range(0,10, 2):
#     el.set_left_child(CompEl(chr(i+97), i))
#     el.set_right_child(CompEl(chr(i+98), i+1))
#     el = el.l_child
#

# bst = BinarySearchTree()
# src = [7, 6, 4, 8, 9, 3, 5, 0, 2, 1, -1]
# for i in src:
#     bst.insert(CompEl(chr(i+97), i), lambda k:k.key)
# bst.print_tree()
# print(bst.search(9,  lambda k:k.key))
# print(bst.search(11,  lambda k:k.key))
# print(bst.search(-2,  lambda k:k.key))
# bst = bst.search(8, lambda k:k.key).delete(lambda k:k.key)
# bst.print_tree()
# bst = bst.search(9, lambda k:k.key).delete(lambda k:k.key)
# bst.print_tree()
# bst = bst.search(0, lambda k:k.key).delete(lambda k:k.key)
# bst.print_tree()
# bst = bst.search(4, lambda k:k.key).delete(lambda k:k.key)
# bst.print_tree()
# bst = bst.search(7, lambda k:k.key).delete(lambda k:k.key)
# bst.print_tree()
# bst.insert(CompEl(chr(8+97), 8), lambda k:k.key)
# bst.print_tree()
# bst = bst.search(6, lambda k:k.key).delete(lambda k:k.key)
# bst.print_tree()

bst = BinarySearchTree()
src = [0, 1, 2, 3, 4, 5]
for i in src:
    bst.insert(CompEl(chr(i+97), i), lambda k:k.key)
bst.print_tree()
bst.get_root().left_rotate()
bst.get_root().left_rotate()
bst.print_tree()
bckrotate = bst.get_root().r_child
bckrotate.left_rotate()
bst.print_tree()
bckrotate.right_rotate()
bst.print_tree()