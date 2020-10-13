class Person:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
    def add_age(self,a):
        if(a<0):
            print("나이 정보 오류")
        else:
            self.__age += a
    def __str__(self):
        return '{0}: {1}'.format(self.__name,self.__age)

def main():
    p = Person('James',22)
    p.add_age(1)
    print(p)

main()