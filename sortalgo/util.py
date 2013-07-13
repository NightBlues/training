__author__ = 'nightblues'

def default_comp(a,b):
    return a>b

def find_min_between(data,a,b,comp=lambda a,b:a>b):
    interval = b-a
    min = a
    for i in range(interval):
        if comp(data[min], data[i+a]):
            min = i+a
    return min

