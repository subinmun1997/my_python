d1={'a':1,'b':2,'c':3}
print(d1)

print(type({}))

d2=dict([('a',1),('b',2),('c',3)])
print(d2)

d3=dict(a=1,b=2,c=3)
print(d3)

d4=dict(zip(['a','b','c'],[1,2,3,]))
print(d4)

print(d1==d2==d3==d4)