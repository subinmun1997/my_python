class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def __str__(self):
        return '{0}: {1}'.format(self.name,self.age)

def main():
    p = Person('James',22)
    print(p)
    p.age -= 1
    print(p)

main()