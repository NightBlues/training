import pytest

from nbt.dyn import calc_chop_price

@pytest.fixture(scope="function")
def price():
	return [0, 1, 3, 4, 5, 8, 9, 10, 11, 12, 13]

def test_simple(price):
	cache = {}

	assert calc_chop_price(price, 4, cache) == (6, [2, 2])
	assert calc_chop_price(price, 10, cache) == (16, [5, 5])
	assert calc_chop_price(price, 7, cache) == (11, [2, 5])
	print cache


def test_timed(price):
	import timeit
	common_s = """\
from nbt.dyn import calc_chop_price
price = {price}
""".format(price=price)
	fast_s = common_s + """\
cache = {}
calc_chop_price(price, 10, cache)
"""
	number = 1000
	time1 = timeit.timeit(
		"calc_chop_price(price, 10, cache)",
		setup=fast_s, number=number)
	time2 = timeit.timeit(
		"calc_chop_price(price, 10)",
		setup=common_s, number=number)
	print time2, time1
	assert time2 > time1
