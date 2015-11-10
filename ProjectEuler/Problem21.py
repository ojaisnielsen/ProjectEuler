def divisors_sum(n):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s += d
    return s

l = range(1, 10001)
visited = set()
s = 0
while len(l) > 0:
    a = l.pop(0)
    if a in visited:
        continue
    b = divisors_sum(a)
    if a == b:
        continue
    c = divisors_sum(b)
    if a == c:
        visited.add(b)
        s += a + b
        print a, b
print s