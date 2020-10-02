from collections import OrderedDict

od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
print(od)

for kv in od.items():
    print(kv)

od=OrderedDict(a=1,b=2,c=3)
print(od)