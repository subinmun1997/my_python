def say1():
    print("hello")

def say2():
    print("hi~")

def caller(fct):
    fct()

caller(say1)
caller(say2)