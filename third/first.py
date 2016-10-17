import random
a = [random.randint(0,100) for x in range(10)]
a.sort()
b = a[::-1]
c = []
for x in range(len(a)):
    c.append(a[x]-b[x])
print a,b
print c
