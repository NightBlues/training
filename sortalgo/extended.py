__author__ = 'nightblues'
import sys
sys.path.append('..')
from datastruct import heap
from sortalgo.orderstat import *

# Hoare's quicksort
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

# Hoare's quicksort; non-recursive
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

def heapsort(data,comp=lambda a,b:a>b):
    for i in reversed(range(len(data)//2)):
        heap.pushdown(data,i)
    last = len(data)-1
    for i in range(len(data)):
        data.enqueue(heap.pop(data,last))
        last-=1


# inserts element into sorted list
def bin_insert_sort(data, comp=lambda a,b:a>b):
    j=1
    while j<len(data):
        insertion_place = j
        # we cant compare element before 0, but if el is lower than everithing - insert before everithing
        if comp(data[0], data[j]):
            data.insert(0, data.pop(j))
            continue
        left=1
        right=j
        i=(left+right)//2
        while right-left>0:
            # if we've found element greater than el end prevous elemtn is lower than el
            if comp(data[i],data[j]) and not comp(data[i-1], data[j]):
                insertion_place = i
                break
            if comp(data[i],data[j]):
                right=i
            else:
                # plus 1 is necessary - left must become equal or more
                # than right if el is greater than others
                left=i+1
            i=(right+left)//2
        data.insert(insertion_place, data.pop(j))
        j+=1


def merge_procedure(data, start1,start2,end, comp=lambda a,b: a>b):
    # merge procedure:
    array1=data[start1:start2+1]
    array2=data[start2+1:end+1]
    first_list_i=0
    second_list_i=0
    i=start1
    # print(array1,array2)
    while i<end+1:
        # print("%d: first_list_i=%d, second_list_i=%d"%(i,first_list_i,second_list_i))
        # if first list is empty
        if first_list_i>len(array1)-1 and second_list_i<len(array2):
            data[i]=array2[second_list_i]
            second_list_i+=1
            i+=1
            continue
        # if second list is empty
        if second_list_i>len(array2)-1 and first_list_i<len(array1):
            data[i]=array1[first_list_i]
            first_list_i+=1
            i+=1
            continue
        # comparing elements from first and second lists
        if comp(array1[first_list_i], array2[second_list_i]):
            data[i]=array2[second_list_i]
            second_list_i+=1
        else:
            data[i]=array1[first_list_i]
            first_list_i+=1
        i+=1
    # print(data[start1:end+1])



def merge_sort(data, start=0, end=None, comp=lambda a,b:a>b):
    if end is None:
        end=len(data)-1
    middle_element = (end+start)//2
    if middle_element-start >=1:
        merge_sort(data, start, middle_element)
    if end-middle_element>1:
        merge_sort(data, middle_element+1, end)
    merge_procedure(data, start, middle_element,end, comp)


