a = range(3)
b = range(10,13)
c = []
for x in a:
    for y in b:
        c.append((x,y))
print c
c = [(x,y) for x in a for y in b]
print c
import itertools
c = itertools.product(a,b)
print list(c)
