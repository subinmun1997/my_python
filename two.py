def two():
    print('two')
    return 2

g = (two()*i for i in range(1,10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))