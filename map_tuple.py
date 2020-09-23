def dbl(e):
    return e*2

tp = (1,2,3)
dbl2 = list(map(dbl,(1,3,5)))
dbl3 = list(map(dbl,tp))

print(dbl2)
print(dbl3)

str = 'string'

st1 = list(map(dbl,str))
st2 = list(map(dbl,'hello'))

print(st1)
print(st2)