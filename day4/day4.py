from math import *
g = []
num = 0
with open("input.txt") as f:
	for r in f.read().split("\n"):
		g.append(r.split(" "))

g = g[0:len(g)-2]
for r in range(0, len(g)):
	g[r] = filter(lambda a: a != '', g[r])
	g[r] = [int(x) for x in g[r]]
	g[r].sort()
	if g[r][0] + g[r][1] > g[r][2]:
		num += 1

print num	 
