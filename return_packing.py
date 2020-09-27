def ret_nums():
    return 1,2,3,4,5

nums = ret_nums()
print(nums)

n,*others = ret_nums()
print(n)
print(others)