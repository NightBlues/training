__author__ = 'nightblues'

import sys
sys.path.append('..')
from datastruct.hashtable import *
from test.util import CompEl

ht = HashTable()
ht.insert("hi there", "hi there value")
for i in range(10):
    ht.insert(chr(i+97), CompEl(chr(i+97),i))

print(ht)
print(ht.search('a'))
print(ht.search('e'))
print(ht.search('hi there'))
for i in range(10, 100):
    ht.insert(chr(i+97), CompEl(chr(i+97),i))
print("collisions made")
print(ht)
print(ht.search('a'))
print(ht.search('e'))
print(ht.search('hi there'))