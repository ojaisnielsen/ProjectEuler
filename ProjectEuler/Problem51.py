from itertools import islice

def prime_candidates():
    yield 2
    yield 3
    i = 1
    while True:
        yield (6 * i) - 1
        yield (6 * i) + 1
        i += 1

def primes():
    posts = []
    for c in prime_candidates():
        for p in posts:
            if c % p == 0:
                break
        else:
            yield c
            posts.append(c)

def digits(n):
    while n > 0:
        yield n - 10 * (n / 10)
        n = n / 10

def bits(n):
    while n > 0:
        yield n ^ ((n >> 1) << 1)
        n = n >> 1

def masks(n):
    d = list(digits(n))
    for i in range (1, 2 ** len(d) - 1):
        mask = list(d)
        j = 0
        v = -1
        bad_mask = False
        for bit in bits(i):
            if bit == 0:
                if not (v == -1 or v == mask[j]):
                   bad_mask = True
                   break
                v = mask[j]
                mask[j] = -1
            j += 1
        if bad_mask:
            continue
        while j < len(d):
            if not (v == -1 or v == mask[j]):
                bad_mask = True
                break
            v = mask[j]
            mask[j] = -1
            j += 1
        if bad_mask:
            continue
        yield mask

k = 8
families = dict()
candidates = dict()
for p in primes():
    for m in masks(p):
        m_key = str(m)
        digit_count = len(m)
        if (digit_count - 1) in candidates:
            print candidates[digit_count - 1]
            exit()
        if m_key in families:
            count, min_p = families[m_key]
            count += 1
            families[m_key] = (count, min_p)
            if count == k:
                print "Candidate: %d" % min_p
                if digit_count in candidates:
                    candidates[digit_count].add(min_p)
                else:
                    candidates[digit_count] = set([min_p])
            if count == k + 1:
                candidates[digit_count].remove(min_p)
                if len(candidates[digit_count]) == 0:
                    del candidates[digit_count]
        else:
            families[m_key] = (1, p)
