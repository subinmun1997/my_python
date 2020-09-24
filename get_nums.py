def get_nums():
    ns = [0,1,0,1,0,1]
    for i in ns:
        yield i

g = get_nums()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))