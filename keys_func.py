d=dict(a=1,b=2,c=3)
print(d)

for k in d.keys():
    print(k,end=', ')

for v in d.values():
    print(v,end=', ')

for kv in d.items():
    print(kv,end=', ')

for k,v in d.items():
    print(k,v,sep=',')
