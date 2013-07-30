__author__ = 'nightblues'
import sys
sys.path.append('..')
from sortalgo.orderstat import *
from random import shuffle
from timeit import Timer

data = [x+1 for x in range(10)]
print(data)
# real_min = min(data)
# real_max = max(data)
# for i in range(50000):
#     shuffle(data)
#     res=find_min_and_max(data)
#     if res != (real_min,real_max):
#        print(data, res)
#        break

tf = Timer("find_min_and_max(data)", """
from random import shuffle
from sortalgo.orderstat import find_min_and_max
data = [x for x in range(100,500, 5)]
shuffle(data)
""")
tf2 = Timer("_minmax(data)", """
from random import shuffle
from sortalgo.orderstat import _minmax
data = [x for x in range(100,500, 5)]
shuffle(data)
""")
# print(tf.timeit(number=100000))
# print(tf2.timeit(number=100000))
#
# t3 = Timer("""
# i=0
# while i< 1000:
#     i+=1
# """)
# t4 = Timer("""
# for i in range(1000):
#     pass
# """)
# print(t3.timeit(number=100000))
# print(t4.timeit(number=100000))
shuffle(data)
print(data)
# randomized_partition_stable(data, 0, len(data))
# randomized_partition(data, 0, len(data))
print(randomized_select(data, 5))
print(data)

# [1, 5)  pivot_el = 3
# data=[0, 4, 2, 1, 3, 5, 8, 9, 7, 6]
# a=1
# b=5
# rnd_i = 4
# rnd_el = data[rnd_i]
# print(" pivot_el = %d "%rnd_el)
# data[rnd_i],data[b-1]=data[b-1],data[rnd_i]
# rnd_i = b-1
# start_of_gt = a-1
# print([data[x] for x in range(a)], " { ",[data[x] for x in range(a,b)]," } ", [data[x] for x in range(b, len(data))])
# print(range(a,b-1))
# for i in range(a,b-1):
#     if data[i]<=rnd_el:
#         start_of_gt+=1
#         data[i],data[start_of_gt]=data[start_of_gt],data[i]
# data[start_of_gt+1], data[rnd_i] = data[rnd_i], data[start_of_gt+1]
# print(start_of_gt+1)