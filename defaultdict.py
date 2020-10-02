from collections import defaultdict

s='robbot'
d = defaultdict(int)

for k in s:
    d[k]+=1

print(d)