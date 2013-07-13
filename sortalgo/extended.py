__author__ = 'nightblues'

from sortalgo.util import *


def qsort(data, comp=lambda a, b: a > b, interval_a=0, interval_b=None):
    if interval_b is None:
        interval_b=len(data)-1
    if interval_b-interval_a<1:
        return

    median_index = int((interval_b - interval_a) / 2)+interval_a
    median_value = data[median_index]

    i = interval_a
    while i <= interval_b:
        if comp(data[i], median_value):
            if i < median_index:
                data.insert(interval_b, data.pop(i))
                median_index -= 1
                continue
        else:
            if i > median_index:
                data.insert(interval_a, data.pop(i))
                median_index += 1
                continue
        i += 1

    if median_index - interval_a > 1:
        qsort(data, comp, interval_a, median_index)
    if interval_b - median_index > 1:
        qsort(data, comp, median_index+1, interval_b)


def qsort_non_recursive(data, comp=lambda a, b: a > b):
    intervals = []
    intervals.append((0,len(data)-1))
    il=0
    while il<len(intervals):
        interval_a=intervals[il][0]
        interval_b=intervals[il][1]
        il+=1

        median_index = int((interval_b - interval_a) / 2)+interval_a
        median_value = data[median_index]

        i = interval_a
        while i <= interval_b:
            if comp(data[i], median_value):
                if i < median_index:
                    data.insert(interval_b, data.pop(i))
                    median_index -= 1
                    continue
            else:
                if i > median_index:
                    data.insert(interval_a, data.pop(i))
                    median_index += 1
                    continue
            i += 1

        if median_index - interval_a > 1:
            intervals.append((interval_a, median_index))
        if interval_b - median_index > 1:
            intervals.append((median_index+1, interval_b))