def birth_only(str):
    pn=str.split("-")
    return pn[0]

p1 = "070609-2011xxx"
p2 = "090716-1012xxx"

print(birth_only(p1))
print(birth_only(p2))