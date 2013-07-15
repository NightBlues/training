# -*- coding: utf-8 -*-
import sys

sys.path.append('..')
from sortalgo.simple import *
from sortalgo.extended import *

from random import shuffle
from time import clock
from copy import deepcopy

def timeFunc(func, times, *args):
    """
        Calculating time for function.
    """
    result = []
    for x in range(times):
        start = clock()
        func(deepcopy(*args))
        result.append(clock() - start)
    return (sum(result) / times)*1000


def timeSort(func, data_size=50, data_count=10):
    """Testing the sort algorithm with given data size and count"""
    print("\nTesting sorting function %s (data size - %d, rand data variations - %d):"%(func.__name__, data_size, data_count))
    test_data_size = data_size
    test_count = data_count
    test_data = []
    for x in range(test_count):
        test_data.append([x for x in range(test_data_size)])
        shuffle(test_data[-1])
    best_data = [x for x in range(test_data_size)]
    worse_data = [test_data_size - x - 1 for x in range(test_data_size)]
    working_data = [x for x in range(test_data_size)]
    shuffle(working_data)
    func(working_data)
    is_working = 'yes' if (working_data==best_data) else 'no'
    print("\tis working:\t\t%s"%is_working,end='\t')
    print("\tbest data:\t\t%.16f"% timeFunc(func, 500, best_data),end='\t')
    print("\tworse data:\t\t%.16f"% timeFunc(func, 500, worse_data),end='\t')
    random_data_time = []
    for a in test_data:
        random_data_time.append(timeFunc(func, 5, a))
    print("\trandom data:\t%.16f"% (sum(random_data_time) / test_count),end='\t')


# working_data = [x for x in range(10)]
# shuffle(working_data)
# print(working_data)
# qsort_non_recursive(working_data)
# print(working_data)

# timeSort(bubble_sort, 50, 50)
# timeSort(choose_sort, 50, 50)
# timeSort(insert_sort, 50, 50)
timeSort(qsort, 200, 5000)
timeSort(qsort_non_recursive, 200, 5000)

