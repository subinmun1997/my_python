class Person:
    def __init__(self,n,a):
        self._name = n
        self._age = a

def main():
    p = Person('James',22)
    print(p.__dict__)
    p.len = 178
    p.adr = 'Korea'
    print(p.__dict__)

main()