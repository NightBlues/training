import sys
sys.path.append('..')
import datastruct.heap as heap
from random import shuffle

# data = [x for x in range(10)]
# shuffle(data)
data=[9, 8, 7, 2, 1, 3, 6, 4, 0, 5]
print(data)
h=[]
for x in data:
    heap.insert(h,x)
    # print(h)
    heap.print_heap(h)
print("===")
last = len(h)-1
h.extend([-15,-16,-17,-18])
print(h)
for i in range(len(h)):
    print(heap.pop(h,last), h)
    last -=1
    # print(heap.print_heap(h))

