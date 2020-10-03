ns=[('Yoon',33),('Lee',12),('Park',29)]

def name(t):
    return t[0]

ns.sort(key=name)
print(ns)