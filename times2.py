def show_all(s):
    for i in s:
        print(i, end=' ')
def times2():
    for i in range(1,10):
       yield 2*i

g = times2()
show_all(g)
