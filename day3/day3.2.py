from math import *
g = []
num = 0
A = []
B = []
C = []
with open("input.txt") as f:
	for r in f.read().split("\n"):
		g.append(r.split(" "))

g = g[0:len(g)-2]
for r in range(0, len(g)):
	g[r] = filter(lambda a: a != '', g[r])
	g[r] = [int(x) for x in g[r]]
	A.append(g[r][0])
	B.append(g[r][1])
	C.append(g[r][2])
W = A + B + C
for r in range(0, len(W), 3):
	t = [W[r], W[r+1], W[r+2]]
	t.sort()
	if t[0] + t[1] > t[2]:
		num += 1

print num	 
