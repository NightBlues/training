# -*- coding: utf-8 -*-
import sys

sys.path.append('..')
from sortalgo.simple import *

from random import shuffle
from time import clock
from copy import deepcopy

def timeFunc(func, times, *args):
    result = []
    for x in range(times):
        start = clock()
        func(deepcopy(*args))
        result.append(clock() - start)
    return (sum(result) / times)*1000


def timeSort(func, data_size=50, data_count=10):
    print "Testing sorting function %s (data size - %d, rand data variations - %d):"%(func.__name__, data_size, data_count)
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
    print "\tis working:\t%s"%is_working
    print "\tbest data:\t%s"% timeFunc(func, 500, best_data)
    print "\tworse data:\t%s"% timeFunc(func, 500, worse_data)
    random_data_time = []
    for a in test_data:
        random_data_time.append(timeFunc(func, 5, a))
    print "\trandom data:\t%s"% (sum(random_data_time) / test_count)


timeSort(bubble_sort, 10, 50)
timeSort(bubble_sort, 100, 25)
timeSort(choose_sort, 10, 50)
timeSort(choose_sort, 100, 25)

