def who(a,b,c):
    print(a,b,c, sep=', ')

who(*[1,2,3])
who(*(0.1,0.2,0.3))
who(*'abc')

p=[4,5,6]
who(*p)