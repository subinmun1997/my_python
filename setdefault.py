s='robbot'
d={}
for k in s:
    d[k] = d.setdefault(k,0)+1

print(d)