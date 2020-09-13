str="YoonSungWoo"
print(str.count("o"))
print(str.count("oo"))

org="Yoon"
lcp=org.lower()
ucp=org.upper()
print(lcp)
print(ucp)
print(org)

org="   MIDDLE   "
cp1= org.lstrip()
cp2= org.rstrip()
print(cp1)
print(cp2)

org="   MIDDLE   "
cp3= org.strip()
print(cp3)
print(org)

org="YoonSungWoo"
rps=org.replace("oo","ee")
print(rps)

org="YoonSungWoo"
rps=org.replace("oo","ee",1)
print(rps)

org="ab cd ef"
ret = org.split()
print(ret)

org="ab_cd_ef"
ret = org.split('_')
print(ret)