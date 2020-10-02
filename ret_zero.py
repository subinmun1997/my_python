from collections import defaultdict

def ret_zero():
    return 0

d = defaultdict(ret_zero)

d['a']
print(d)

d = defaultdict(lambda :7)
d['z']
print(d)