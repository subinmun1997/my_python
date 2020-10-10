t=(1,2,3)
print(len(t)) # t.__len__()

itr = iter(t) # t.__lter__()
for i in itr:
    print(i,end=' ')

s = str(t) # t.__str__()
print(s)