n = 2000000
def candidates(n):
    yield 2
    yield 3
    i = 1
    while True:
        p = (6 * i) - 1
        if p < n:
            yield p
        else:
            return
        p = (6 * i) + 1
        if p < n:
            yield p
        i = i + 1

def sieve(candidates):
    posts = []
    for c in candidates:
        for p in posts:
            if c % p == 0:
                break
        else:
            yield c
            posts.append(c)

k = 0
s = 0
for p in sieve(candidates(n)):
    k = k + 1
    if k % 100 == 0:
        print k
    s = s + p

print s
