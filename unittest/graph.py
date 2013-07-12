# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from datastruct.graph import *

ver1 = Vertex('a')
ver2 = Vertex('b')
ver3 = Vertex()
ver3.setValue('a')
print((ver1,ver2,ver3))
vertices = [ver1,ver2,ver3,ver1]
print(vertices)
print(vertices[0]==vertices[3])
print(vertices[0]==vertices[2])
print(vertices[0]==vertices[1])
vertices[3].setValue('c')
print(vertices)