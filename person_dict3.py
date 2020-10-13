class Person:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a

def main():
    p = Person('James',22)
    print(p.__dict__)

main()