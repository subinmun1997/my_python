class Natural:
    def __init__(self,n):
        if(n<1):
            self.__n = 1
        else:
            self.__n = n
    def getn(self): # 값 꺼내기 getter
        return self.__n
    def setn(self,n): # 값 수정하기 setter
        if(n<1):
            self.__n = 1
        else:
            self.__n = n

def main():
    n = Natural(-3)
    print(n.getn())
    n.setn(2)
    print(n.getn())

main()