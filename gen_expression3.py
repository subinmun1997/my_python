def show_all(s):
    for i in s:
        print(i, end=' ')

show_all(2*i for i in range(1,10))