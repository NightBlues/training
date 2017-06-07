
import itertools
from decimal import Decimal


def gen_numbers(n):
    return itertools.product(range(n), range(n), range(n))


def expression(a, b, c):
    a, b, c = Decimal(a), Decimal(b), Decimal(b)
    if (b + c) * (a + c) * (a + b) == 0:
        return None
    return (a / (b + c)) + (b / (a + c)) + (c / (a + b))


if __name__ == '__main__':
    for a, b, c in gen_numbers(100):
        if b == c == 0:
            print "Current: ", a, b, c
        if expression(a, b, c) == 4:
            print a, b, c
            break
