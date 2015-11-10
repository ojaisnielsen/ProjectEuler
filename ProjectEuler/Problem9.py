n = 1000
for c in range(1, n/2):
    for b in range(1, c):
        a = n - c - b
        if a ** 2 + b ** 2 == c ** 2:
            print a, b, c, a * b * c
