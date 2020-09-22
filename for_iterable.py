for i in [1,2,3]:
    print(i, end=' ')

ir = iter([1,2,3])
while True:
    try:
        i = next(ir)
        print(i, end=' ')
    except StopIteration:
        break