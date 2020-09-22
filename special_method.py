ds=[1,2,3]
ir = iter(ds)
print(next(ir))
print(next(ir))

ds=[1,2,3]
ir=ds.__iter__()
print(ir.__next__())
print(ir.__next__())