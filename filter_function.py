def is_odd(n):
    return n%2 #홀수면 True 짝수면 False

st=[1,2,3,4,5]
ost=list(filter(is_odd,st))
print(ost)