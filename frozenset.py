A=frozenset(['a','c','d','f'])
B=frozenset(['a','b','d','c'])
print(A)
print(B)
print(A-B)
print(A|B)
print(A==B)
print(A&B)

print('a' in A)

for c in A&B:
    print(c, end=' ')