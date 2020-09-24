import sys

def pows(s):
    r=[]
    for i in s:
        r.append(i**2)
    return r

st = pows([1,2,3,4,5,6,7,8,9])
for i in st:
    print(i, end=' ')

print(sys.getsizeof(st))