u = 1
v = 2
s = 0
while v <= 4000000:
    if v % 2 == 0:
        s = s + v
    t = v
    v = u + v
    u = t

print s