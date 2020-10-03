nums=[(3,1),(2,9),(0,5)]
nums.sort(key = lambda t:t[0]+t[1], reverse=True)
print(nums)