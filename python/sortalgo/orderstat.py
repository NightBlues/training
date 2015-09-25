__author__ = 'nightblues'
from random import randint

def find_min_between(data,a,b,comp=lambda a,b:a>b):
    interval = b-a
    min_ = a
    for i in range(interval):
        if comp(data[min_], data[i+a]):
            min_ = i+a
    return min_

def minmax(data, comp=lambda a,b:a>b):
    if len(data)==0:
        return None
    el = data[0]
    for i in data:
        if comp(el, i):
            el = i
    return el

def _min(data):
    if len(data)==0:
        return None
    min_el=data[0]
    # i = 1
    # while i<len(data):
    #     if min_el>data[i]:
    #         min_el = data[i]
    #     i+=1
    for i in data:
        if min_el>i:
            min_el=i
    return min_el

def _max(data):
    if len(data)==0:
        return None
    max_el=data[0]
    # i =1
    # while i<len(data):
    #     if max_el<data[i]:
    #         max_el = data[i]
    #     i+=1
    for i in data:
        if max_el<i:
            max_el=i
    return max_el

def _minmax(data):
    return _min(data), _max(data)

def find_min_and_max(data):
    if len(data)==0:
        return None
    if len(data)==1:
        return data[0], data[0]
    min_el, max_el = data[0],data[1]
    if max_el<min_el:
        max_el,min_el=min_el,max_el
    i=2 if len(data)%2==0 else 1
    while i+1<len(data):
        if data[i]>data[i+1]:
            if min_el>data[i+1]:
                min_el = data[i+1]
            if max_el<data[i]:
                max_el = data[i]
        else:
            if min_el>data[i]:
                min_el = data[i]
            if max_el<data[i+1]:
                max_el = data[i+1]
        i+=2
    return min_el, max_el

# part of qsort.
def randomized_partition_stable(data, a,b):
    if b-a==1:
        return a
    rnd_i = randint(a, b-1)
    data[rnd_i],data[b-1]=data[b-1],data[rnd_i]
    rnd_i=b-1
    i=0
    while i < rnd_i:
        if data[i]>data[rnd_i]:
            j=i
            cur = data[i]
            while j<b-1:
                data[j]=data[j+1]
                j+=1
            data[b-1]=cur
            rnd_i-=1
            continue
        i+=1
    return rnd_i

# part of qsort. fast but non stable
def randomized_partition_my(data, a, b):
    if b-a==1:
        return a
    rnd_i = randint(a, b-1)
    data[rnd_i],data[b-1]=data[b-1],data[rnd_i]
    rnd_i = b-1
    i=0
    while i<rnd_i:
        if data[i]>data[rnd_i]:
            if i+1==rnd_i:
                data[rnd_i], data[i] = data[i], data[rnd_i]
            else:
                data[rnd_i], data[rnd_i-1] = data[rnd_i-1], data[rnd_i]
                data[rnd_i], data[i] = data[i], data[rnd_i]
                rnd_i-=1
                continue
        i+=1
    return rnd_i

# part of qsort. fast, non stable, lomuto
def randomized_partition(data, a, b):
    if b-a==1:
        return a
    rnd_i = randint(a, b-1)
    rnd_el = data[rnd_i]
    data[rnd_i],data[b-1]=data[b-1],data[rnd_i]
    rnd_i = b-1
    start_of_gt = a-1
    for i in range(a, b-1):
        if data[i]<=rnd_el:
            start_of_gt+=1
            data[i],data[start_of_gt]=data[start_of_gt],data[i]
    data[start_of_gt+1], data[rnd_i] = data[rnd_i], data[start_of_gt+1]
    return start_of_gt+1


# return i'th order statistic
def randomized_select(data, i, a=None, b=None):
    if a is None:
        a = 0
    if b is None:
        b = len(data)
    if a==b :
        return data[a]
    q = randomized_partition(data, a, b)
    if q == i:
        return data[q]
    if q > i:
        return randomized_select(data, i, a, q)
    else:
        return randomized_select(data, i, q+1, b)


