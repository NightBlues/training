__author__ = 'nightblues'
import sys
sys.path.append('..')
from elemalgo.simple import *
from random import randint
from timeit import Timer

# for x in range(5):
#     a,b=randint(1,100),randint(1,100)
#     print('%d gcd %d=%d'%(a,b,euclid(a,b)))
#
# for x in range(5):
#     a=2
#     n=randint(0,15)
#     print('%d^%d=%d'%(a,n,binpow(a,n)))
#     print('%d^%d=%d'%(a,n,binpow_non_recursive(a,n)))


max_algo_res = eratosthenes_m(10000)
my_res = eratosthenes(10000)
if my_res == max_algo_res:
    print("it works!")
else:
    print("it doesn't work=(")


my = Timer('eratosthenes(500)', """
import sys
sys.path.append('..')
from elemalgo.simple import eratosthenes
""")
max_algo = Timer('eratosthenes_m(500)', """
import sys
sys.path.append('..')
from elemalgo.simple import eratosthenes_m
""")
print(my.timeit(number=100000))
print(max_algo.timeit(number=100000))


