__author__ = 'nightblues'
from datastruct.hashfunc import *
from datastruct.linkedlist import LinkedList


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
        index = self.hash_from_string(key)
        if self.data[index] is None:
            self.data[index] = LinkedList(HashTableElement(key, value))
        else:
            self.data[index].insert(HashTableElement(key, value))
            self.data[index] = self.data[index].prev()

    def search(self, key):
        return self.data[self.hash_from_string(key)].search(key, key=lambda k: k.key)

    def delete(self, element):
        if element.isOnly():
            self.data[self.hash_from_string(element.value.key)] = None
        else:
            element.delete()

    def __unicode__(self):
        return "<HashTable, \n%s\n/HashTable>\n" % ('\n'.join(['\t'+str(x) for x in self.data]))

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class HashTableElement():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __unicode__(self):
        return "<HashTableElement, (%s, %s)" % (self.key, self.value)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()