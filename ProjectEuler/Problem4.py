from math import log

def nth_digit(i, n):
    return (i / 10 ** n) - 10 * (i / 10 ** (n + 1))

def is_palindromic(n):
    i = int(log(n, 10)) + 1
    for j in range(0, i / 2):
        if nth_digit(n, j) != nth_digit(n, i - j - 1):
            return False
    return True

integers = range(100, 1000)
max = 0
for i in integers:
    for j in integers:
        n = i * j
        if n > max and is_palindromic(n):
            max = n

print max
