def gen_num():
    print('first number')
    yield 1
    print('second number')
    yield 2
    print('third number')
    yield 3

gen = gen_num()
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
