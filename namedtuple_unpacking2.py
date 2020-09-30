from collections import namedtuple

def show(n1,n2):
    print(n1,n2)

Tri = namedtuple('Tri','bottom height')
t = Tri(3,8)
show(*t)