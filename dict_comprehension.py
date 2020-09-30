r1=[1,2,3,4,5]
r2=[x*2 for x in r1]
print(r2)

d1=dict(a=1,b=2,c=3)
d2={k:v*2 for k,v in d1.items()}
print(d2)
d3={k:v*2 for k,v in d2.items()}
print(d3)

r1=[1,2,3,4,5]
r2=[x*2 for x in r1 if x%2]
print(r2)

d1=dict(a=1,b=2,c=3,d=4)
print(d1)
d2={k:v for k,v in d1.items() if v%2}
print(d2)

ks=['a','b','c','d']
vs=[1,2,3,4]
d={k:v for k,v in zip(ks,vs)}
print(d)
d2={k:v for k,v in zip(ks,vs) if v%2}
print(d2)