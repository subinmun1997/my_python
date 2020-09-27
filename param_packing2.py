def sum(*nums):
    s=0
    for i in nums:
        s+=i
    return s

print(sum(1,2,3))
print(sum(1,2,3,4))
print(sum(1,2,3,4,5))