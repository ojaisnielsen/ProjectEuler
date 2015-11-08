def collatz(n):
	yield n
	while n > 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3 * n + 1
		yield n

max = 0
arg_max = 0
for a in range(1, 1000000):
	l = sum(1 for x in collatz(a))
	if a % 10000 == 0:
		print a, max
	if l > max:
		max = l
		arg_max = a

print arg_max, max


