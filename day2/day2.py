from math import *

def condition(A):
	for n in range(0,2):
		if A[n] < 0:
			A[n] = 0
		elif A[n] > 2:
			A[n] =  2
	return A

g = []
with open("input.txt") as f:
	g = f.read().split("\n")

data = [[1,2,3],[4,5,6],[7,8,9]]
pos = [1,1]
for i in range(0, len(g) - 1):
	for j in range(0, len(g[i])):
		if g[i][j] == 'D':
			pos[1] += 1
		elif g[i][j] == 'U':
			pos[1] -= 1
		elif g[i][j] == 'R':
			pos[0] += 1
		elif g[i][j] == 'L':
			pos[0] -= 1
		pos = condition(pos)
	print data[pos[1]][pos[0]],
