def who(a,b,c):
    print(a,b,c,sep=', ')

d=dict(a=1,b=2,c=3)
who(*(d.items()))