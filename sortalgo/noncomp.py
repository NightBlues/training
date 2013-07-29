__author__ = 'nightblues'
from sortalgo.util import *

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