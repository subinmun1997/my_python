ns=[('Yoon',33),('Lee',12),('Park',29)]

def age(t):
    return t[1]

ns.sort(key=age)
print(ns)

ns.sort(key=age, reverse=True)
print(ns)