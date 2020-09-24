st=list(range(1,11))
print(st)
fst=list(map(lambda n : n**2,filter(lambda n : n%2,st)))
print(fst)