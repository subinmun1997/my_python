def fct_fac(n):
    return lambda x : x**n

f2 = fct_fac(2)
f3 = fct_fac(3)
print(f2(4))
print(f3(4))