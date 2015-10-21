i = 2
p = 0
n = 0
f = 1
while n < 10001:
    if (f + 1) % i == 0:
        p = i
        n = n + 1
        if (n % 100 == 0):
            print n, p
    f = f * i
    i = i + 1

print n, p
