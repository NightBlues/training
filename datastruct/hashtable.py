__author__ = 'nightblues'
from datastruct.hashfunc import *


class HashTable():

    def __init__(self):
        self.table_size = 100
        self.data = [None for i in range(self.table_size)]
        self.h = division_hash(self.table_size)

    def hash_from_string(self, key):
        res = 0
        if isinstance(key, str):
            for c in key:
                res = res << 8 | ord(c)
        else:
            res = key
        return self.h(res)


    def insert(self, key, value):
        self.data[self.hash_from_string(key)] = value

    def search(self, key):
        return self.data[self.hash_from_string(key)]

    def delete(self, element):
        self.data[element] = None

    def __unicode__(self):
        return "<HashTable, \"%s\"" % (self.data)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()
