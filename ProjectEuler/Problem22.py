import csv

names = list(csv.reader(open("p022_names.txt")))[0]

def swap(l, i, j):
    a = l[i]
    l[i] = l[j]
    l[j] = a

def quick_sort(l, comp, start = -1, end = -1):
    if start < 0:
        start = 0
    if end < 0:
        end = len(l)
    if end - start <= 1:
        return
    p = l[end - 1]
    i = start
    j = end - 1
    while i < j:
        while i < j and comp(l[i], p) < 0:
            i += 1
        while i < j and comp(l[i], p) > 0:
            swap(l, i, j - 1)
            swap(l, j - 1, j)
            j -= 1
    quick_sort(l, comp, start, j)
    quick_sort(l, comp, j, end)

def word_comp(a, b):
    i = 0
    while i < len(a) and i < len(b):
        if ord(a[i]) < ord(b[i]):
            return -1
        elif ord(a[i]) > ord(b[i]):
            return 1
        i += 1
    if len(a) == len(b):
        return 0
    elif i >= len(a):
        return -1
    else:
        return 1

def score(a):
    s = 0
    for l in a:
        s += ord(l) - ord("A") + 1
    return s

quick_sort(names, word_comp)
i = 1
s = 0
for name in names:
    s += i * score(name)
    i += 1
print s