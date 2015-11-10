digits = [1]

for i in range (1, 1001):
	r = 0
	for j in range(0, len(digits)):
		digits[j] = digits[j] * 2 + r
		if digits[j] >= 10:
			r = 1
			digits[j] = digits[j] - 10
		else:
			r = 0
	if r > 0:
		digits.append(r)
		r = 0

print sum(digits)



