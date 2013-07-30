__author__ = 'nightblues'
import sys
sys.path.append('..')

from datastruct.linkedlist import *
from test.util import CompEl

elems = ['hi', 'there', 'elem5', 'elemental','element7']
linlist = LinkedList()
for x in elems:
    linlist.append(x)

for e in linlist:
    print(e)

bad_el = linlist.search("elem5")
bad_el.delete()
del bad_el
print(linlist.get_tail().delete())
linlist.search("elemental").insert("instance of")
for e in linlist:
    print(e)

