d=dict(a=1,b=2,c=3)
vo = d.items()

for kv in vo:
    print(kv,end=' ')

d['a']+=3
d['c']-=2

for kv in vo:
    print(kv,end=' ')