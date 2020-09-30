from collections import namedtuple

Tri = namedtuple("Triangle",["bottom","height"])
t = Tri(3,7)
print(t[0],t[1])
print(t.bottom,t.height)