def digits(n):
    k = 0
    l = 1
    while n > 0:
        yield n - 10 * (n / 10)
        n = n / 10

def multiplyByDigit(n, d):
    r = 0
    for a in n:
        a *= d
        a += r
        r = a / 10
        yield a % 10
    if r > 0:
        yield r

def sumDigits(n, m):
    r = 0
    i = 0
    while i < len(n) or i < len(m):
        d = r
        if i < len(n):
            d += n[i]
        if i < len(m):
            d += m[i]
        r = d / 10
        yield d % 10
        i += 1
    if r > 0:
        yield r

n = [1]
for i in range(0, 100):
    o = 0
    t = []
    for d in digits(i + 1):
        r = 0
        t = sumDigits(list(t), [0] * o + list(multiplyByDigit(n, d)))
        o += 1
    n = list(t)

print sum(n)