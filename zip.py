z = zip(['a','b','c'],[1,2,3])
for i in z:
    print(i,end=', ')

z = zip(('a','b','c'),(1,2,3))
for i in z:
    print(i,end=', ')

z = zip('abc',(1,2,3))
for i in z:
    print(i,end=', ')