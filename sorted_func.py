org=[('Yoon',33),('Lee',12),('Park',29)]
cpy = sorted(org, key=lambda t:t[1],reverse=True)
print(org)
print(cpy)