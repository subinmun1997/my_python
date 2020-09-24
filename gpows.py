import sys

def gpows(s):
    for i in s:
        yield i**2

st = gpows([1,2,3,4,5,6,7,8,9])
for i in st:
    print(i, end=' ')

print(sys.getsizeof(st))