cache = {}
def letters(n):
	if not n in cache:
		if n == 0:
			cache[n] = 0
		elif n in [1, 2, 6, 10]:
			cache[n] = 3
		elif n in [3, 7, 8, 40, 50, 60]:
			cache[n] = 5
		elif n in [4, 5, 9]:
			cache[n] = 4
		elif n in [11, 12, 20, 30, 80, 90]:
			cache[n] = 6
		elif n in [13, 14, 18, 19]:
			cache[n] = 8
		elif n in [15, 16, 70]:
			cache[n] = 7
		elif n in [17]:
			cache[n] = 9
		elif n < 100:
			cache[n] = letters(10 * (n / 10)) + letters(n - 10 * (n / 10))
		elif n < 1000:
			m = n / 100
			cache[n] = letters(m) + 7
			if n > 100 * m:
				cache[n] = cache[n] + 3 + letters(n - 100 * m)
		else:
			cache[n] = 11
	return cache[n]

s = 0
for i in range(1, 1001):
	s = s + letters(i)
print s
