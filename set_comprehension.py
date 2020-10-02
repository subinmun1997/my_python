s1={x for x in range(1,11)}
print(s1)

s2={x**2 for x in s1}
print(s2)

s3={x for x in s2 if x<50}
print(s3)