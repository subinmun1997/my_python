def adder2(n1,n2):
    return n1+n2

def adder3(n1,n2,n3):
    return n1+n2+n3

def adder_deco(func):
    def ad(*args):
        print(*args, sep='+', end=' ')
        print("= {0}".format(func(*args)))
    return ad

adder2 = adder_deco(adder2)
adder2(3,4)
adder3 = adder_deco(adder3)
adder3(1,2,3)