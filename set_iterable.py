A=set(['a','c','d','f'])
B=set('fdca')
print(A)
print(B)

print(A==B)
print('a' in A)
print('b' not in A)

for c in A&B:
    print(c,end=' ')