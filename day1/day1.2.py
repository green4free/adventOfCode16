from math import *
step = 90
deg = step
x = 0
y = 0
U = 0
f = open("input.txt")
a = f.readline().split(', ')
f.close()
g = []
for t in a:
	if t[0] == 'R':
		deg -= step
	elif t[0] == 'L':
		deg += step
	for u in range(int(t[1:])):
		x += int(cos(radians(deg)))
		y += int(sin(radians(deg)))
		if ((x,y) in g):
			U = 1			
			break
		else:
			g.append((x,y))
	if U:
		break
print abs(x) + abs(y)
