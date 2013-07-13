__author__ = 'NightBlues'

from sortalgo.util import *

# bubble sort
def bubble_sort(data, comp=lambda a, b: a > b):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if comp(data[j], data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]

# sort by choosing
def choose_sort(data, comp=lambda a, b: a > b):
    for i in range(len(data)):
        min = find_min_between(data, i, len(data), comp)
        data[i], data[min] = data[min], data[i]


# sort by inserting element onto appropriate place
def insert_sort(data, comp=lambda a, b: a > b):
    for i in range(len(data) - 1):
        # we are starting from the second element
        index = i + 1
        # if we do not find element we will insert into the end
        index_to_insert = index
        for j in range(index):
            if comp(data[j], data[index]):
                index_to_insert = j
                break
        if not index_to_insert == index:
            data.insert(index_to_insert, data.pop(index))
