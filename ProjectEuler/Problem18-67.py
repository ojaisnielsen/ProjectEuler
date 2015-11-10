# from io import open
# t = []
# with open("p067_triangle.txt") as f:
# 	for line in f.readlines():
# 		row = [int(s) for s in line.split()]
# 		t.append(row)

t = [
[75], 
[95, 64], 
[17, 47, 82], 
[18, 35, 87, 1], 
[2, 4, 82, 47, 65], 
[19, 1, 23, 75, 3, 34], 
[88, 2, 77, 73, 7, 63, 67], 
[99, 65, 4, 28, 6, 16, 7, 92], 
[41, 41, 26, 56, 83, 4, 8, 7, 33], 
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
[7, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
[91, 71, 52, 38, 17, 14, 91, 43, 58, 5, 27, 29, 48], 
[63, 66, 4, 68, 89, 53, 67, 3, 73, 16, 69, 87, 4, 31], 
[4, 62, 98, 27, 23, 9, 7, 98, 73, 93, 38, 53, 6, 4, 23], 
]

c = []
for row in t:
	c.append([None] * len(row))



def find_max(t, i, j):
	if c[i][j] == None:
		if i == 0:
			c[i][j] = t[0][0]
		else:
			sub_max = 0
			if j < i:
				sub_max = find_max(t, i - 1, j)
			if j > 0:
				sub_max = max(sub_max, find_max(t, i - 1, j - 1))
			c[i][j] = sub_max + t[i][j]
	return c[i][j]

print max(find_max(t, len(t) - 1, j) for j in range(0, len(t[-1])))