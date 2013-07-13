__author__ = 'NightBlues'

def swap(a,b):
    pass

# bubble sort
def bubble_sort(data, comp=lambda a,b:a>b):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if comp(data[j], data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    return data

def find_min_between(data,a,b,comp=lambda a,b:a>b):
    interval = b-a
    min = a
    for i in range(interval):
        if comp(data[min], data[i+a]):
            min = i+a
    return min


def choose_sort(data, comp=lambda a,b:a>b):
    for i in range(len(data)):
        min = find_min_between(data, i, len(data), comp)
#        for j in range(len(data)-i):
#            if comp(data[min], data[j+i]):
#                min = j+i
        data[i], data[min] = data[min], data[i]
    return data