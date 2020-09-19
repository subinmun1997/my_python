def min_max(d):
    d = list(d)
    d.sort()
    print(d[0],d[-1],sep=',')

t = (2,7,5,9,0)
min_max(t)
print(t)