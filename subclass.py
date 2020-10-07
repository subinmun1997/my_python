class A:
    pass

class Z(A):
    pass

print(issubclass(Z,A))
print(issubclass(Z,object))
print(issubclass(A,object))
print(issubclass(type,object))