def show(s):
    print(s)

ref = show
ref('hi~')

ref = lambda s : print(s)
ref('oh~')