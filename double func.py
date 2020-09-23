def fct_fac(n):
    def exp(x):
        return x**n
    return exp

f2 = fct_fac(2)
f3 = fct_fac(3)

print(f2(4))
print(f3(4))