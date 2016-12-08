from math import *
g = []
with open("input.txt") as f:
	g = f.read().split("\n")

data = [[0,0,0,0,0,0,0],[0,0,0,'1',0,0,0],[0,0,'2','3','4',0,0],[0,'5','6','7','8','9',0],[0,0,'A','B','C',0,0],[0,0,0,'D',0,0,0],[0,0,0,0,0,0,0]]
pos = [3,1]
t = ""
for i in range(0, len(g) - 1):
	for j in range(0, len(g[i])):
		if g[i][j] == 'D':
			pos[1] += 1
			if 0 == data[pos[1]][pos[0]]:
				pos[1] -= 1
		elif g[i][j] == 'U':
			pos[1] -= 1
			if 0 == data[pos[1]][pos[0]]:
                                pos[1] += 1
		elif g[i][j] == 'R':
			pos[0] += 1
			if 0 == data[pos[1]][pos[0]]:
                                pos[0] -= 1
		elif g[i][j] == 'L':
			pos[0] -= 1
			if 0 == data[pos[1]][pos[0]]:
                                pos[0] += 1
	t += data[pos[1]][pos[0]]

print t
