from math import sqrt

def primes(n):
    integers = range(2, n + 1)
    while len(integers) > 0:
        p = integers[0]
        yield p
        if p ** 2 > integers[-1]:
            break
        i = 0
        while i < len(integers):
            if integers[i] % p == 0:
                del integers[i]
            else:
                i = i + 1

n = 600851475143
print "%d = " % n
for p in primes(10000):
    k = 0
    while n % p == 0:
        n = n / p
        k = k + 1
    if k > 0:
        print "%d ^ %d *" % (p, k)

print n