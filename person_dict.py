class Person:
    def __init__(self,n,a):
        self._name = n
        self._age = a

def main():
    p = Person('James',22)
    print(p.__dict__)

main()