from collections import namedtuple

Tri = namedtuple('Tri','bottom height')
t = Tri(12,79)
a,b = t
print(a,b)