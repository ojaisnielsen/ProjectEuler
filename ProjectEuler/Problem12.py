
def sieve(candidates):
    posts = []
    for c in candidates:
        for p in posts:
            if c % p == 0:
                break
        else:
            yield c
            posts.append(c)

cache = {}
def prime_facts(n):
    if n not in cache:
        m = n
        facts = []
        for p in sieve([2] + range(3, n + 1, 2)):
            k = 0
            while m % p == 0:
                k = k + 1
                m = m / p
            if k > 0:
                facts.append((p, k))
        cache[n] = facts
    return cache[n]

def divisors(f):
    return reduce(lambda x, y: x * y, [k + 1 for p, k in f], 1)

max = 0
n = 0
while max < 500:
    n = n + 1
    t = (n * (n + 1)) / 2
    d = 0
    if n % 2 == 0:
        d = divisors(prime_facts(n / 2) + prime_facts(n + 1))
    else:
        d = divisors(prime_facts(n) + prime_facts((n + 1) / 2))
    if d > max:
        max = d
        print t, d