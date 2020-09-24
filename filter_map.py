st=list(range(1,11))
fst=list(filter(lambda n : not(n%3),map(lambda x : x**2,st)))
print(fst)