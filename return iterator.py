ir = iter([1,2,3])
ir2 = iter(ir)

print(ir is ir2)
print(id(ir))
print(id(ir2))