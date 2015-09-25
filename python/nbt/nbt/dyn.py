

def calc_chop_price(price, n, cache={}):
	if n in cache:
		return cache[n]

	cache[0], cache[1] = (0, []), (1, [1])
	for i in range(1, n + 1):
		choices = range(i)
		max_idx = max(choices, key=lambda j: cache[j][0] + price[i - j])
		max_val = cache[max_idx][0] + price[i - max_idx]
		cache[i] = (max_val, cache[max_idx][1] + [i - max_idx])

	return cache[i]
