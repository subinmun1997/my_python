def gen_for():
    for i in [1,2,3]:
        yield i

g = gen_for()
print(next(g))
print(next(g))
print(next(g))
