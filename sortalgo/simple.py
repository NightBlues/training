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


def insert_sort_m(data, comp=lambda a, b: a > b):
    i = 1
    while i < len(data):
        j = i - 1
        while j >= 0 and comp(data[j], data[j + 1]):
            data[j], data[j + 1] = data[j + 1], data[j]
            j -= 1
        i += 1


def insert_sort_m2(data, comp=lambda a, b: a > b):
    i = 1
    while i < len(data):
        cur = data[i]
        j = i - 1
        while j >= 0 and comp(data[j], cur):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = cur
        i += 1


def counting_sort(data, key=lambda a: a):
    max_el = key(minmax(data, lambda a, b: key(a) < key(b)))
    count_list = [0 for i in range(max_el + 1)]
    for i in data:
        count_list[key(i)] += 1
    i = 1
    while i < len(count_list):
        count_list[i] += count_list[i - 1]
        i += 1
    result_list = [None for i in data]
    for i in reversed(range(len(data))):
        result_list[count_list[key(data[i])] - 1] = data[i]
        count_list[key(data[i])] -= 1
    i = 0
    for x in result_list:
        data[i] = x
        i += 1


def radix_sort(data, r=2, key=lambda a: a):
    def get_radix_func(r, i, key):
        sh_c = r * i

        def radix_func(a):
            return (key(a) >> sh_c) - (key(a) >> sh_c + r << r)

        return radix_func

    max_el = key(minmax(data, lambda a, b: key(a) < key(b)))
    i = 0
    while max_el >> (r * i) > 0:
        get_cur_radix = get_radix_func(r, i, key)
        counting_sort(data, key=get_cur_radix)
        i += 1


def clever_radix_sort(data, key=lambda a: a):
    max_el = max_el_acc = key(minmax(data, lambda a, b: key(a) < key(b)))
    r = 0
    b = 0
    while max_el_acc != 0:
        max_el_acc = max_el_acc >> 1
        b += 1
    from math import log2

    lgn = int(log2(len(data)))
    if b < lgn:
        r = b
    else:
        r = lgn

    radix_sort(data, r, key)
