def show_all(s):
    for i in s:
        print(i, end=' ')

g = (2*i for i in range(1,10))
show_all(g)