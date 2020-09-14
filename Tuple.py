nums=(3,2,5,7,1)
print(len(nums))
print(max(nums))
print(min(nums))

nums=(1,2,3,1,2)
print(nums.count(2))
print(nums.index(1))

nums=(1,2,3)
r = 3 in nums
print(r)

r = 2 not in nums
print(r)

print(nums+(4,5))
print(nums*2)
print(nums[0:3])
print(nums)

for i in (1,3,5,7,9):
    print(i,end=' ')