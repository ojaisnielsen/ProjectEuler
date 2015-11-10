b = 2
n = 2
s_b = 2
s_n = 1
while n < 1000000000000:
    while True:
        if s_b < s_n:
            s_b += 2 * b
            b += 1
        else:
            s_n += n
            n += 1
        if n % 1000000000 == 0:
            print n
        if s_b == s_n:
            break
    print b, n

    