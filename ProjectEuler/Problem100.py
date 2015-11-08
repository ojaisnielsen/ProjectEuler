from math import log, exp

def f(b, n):
	return log(b) + log(b - 1) - log(n) - log(n - 1) + log(2)

def fp(b):
	return (1.0/b) + (1.0 / (b - 1))

def g(b, n):
	return  2 * b * (b - 1) - n * (n - 1)

n = 1000000000000
while True:
	b = n / 2

	for i in range(1, 1000):
		b = b - f(b, n) / fp(b)


	b = int(round(b))
	print g(b, n)
	if g(b, n) == 0:
	 	print n, b, g(b, n)
	 	break
	 	

	n = n + 1
