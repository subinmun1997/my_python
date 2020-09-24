def get_nums():
    ns = [0,1,0,1,0,1]
    yield from ns

g = get_nums()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))