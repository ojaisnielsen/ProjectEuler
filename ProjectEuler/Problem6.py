a = range(1, 101)
print sum([i * j for i in a for j in a if i != j])