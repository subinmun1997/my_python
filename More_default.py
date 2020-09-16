def have_default_value(n1,n2,n3="df1",n4="df2"):
    print(n1,n2,n3,n4)

r = have_default_value(1,2,3,4)
print(r)
r2 = have_default_value(1,2)
print(r2)