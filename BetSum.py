def bet_sum(num1,num2):
    sum=0
    for i in range(num1+1,num2):
        sum+=i
    return sum

print(bet_sum(2,5))