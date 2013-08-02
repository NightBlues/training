__author__ = 'nightblues'
import sys
sys.path.append('..')
from datastruct.tree import *
from test.util import CompEl

bt = BinaryTree()
el = bt
for i in range(0,10, 2):
    el.set_left_child(CompEl(chr(i+97), i))
    el.set_right_child(CompEl(chr(i+98), i+1))
    el = el.l_child

for x in bt.bfs():
    print(x)