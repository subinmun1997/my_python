from collections import OrderedDict

od=OrderedDict(a=1,b=2,c=3)
for kv in od.items():
    print(kv, end=' ')

od.move_to_end('b')
for kv in od.items():
    print(kv,end=' ')

od.move_to_end('b', last=False)
for kv in od.items():
    print(kv, end=' ')