n = 20
a = 1
for i in range(n + 1, 2 * n + 1):
	a = a * i

b = 1
for i in range(1, n + 1):
	b = b * i

print a / b
