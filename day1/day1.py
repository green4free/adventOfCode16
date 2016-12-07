from math import *
step = 90
deg = step
pos = [0,0]
f = open("input.txt")
a = f.readline().split(', ')
f.close()
for t in a:
	if t[0] == 'R':
		deg -= step
	elif t[0] == 'L':
		deg += step
	pos[0] += int(cos(radians(deg))) * int(t[1:])
	pos[1] += int(sin(radians(deg))) * int(t[1:])

print abs(pos[0]) + abs(pos[1])
