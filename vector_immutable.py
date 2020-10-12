n=5
print(id(n))
n+=1
print(id(n))

n=[1,2]
print(id(n))
n+=[3]
print(n)
print(id(n))