class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def add_age(self,a):
        if(a<0):
            print("나이 정보 오류")
        else:
            self.age += a
    def __str__(self):
        return '{0}: {1}'.format(self.name,self.age)

def main():
    p = Person('James',22)
    print(p)
    p.add_age(1)
    print(p)

main()
