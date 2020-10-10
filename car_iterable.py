class Car:
    def __init__(self,id):
        self.id = id
    def __iter__(self):
        return iter(self.id)

def main():
    c = Car("32러5234")
    for i in c:
        print(i, end=' ')

main()