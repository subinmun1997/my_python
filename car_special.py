class Car:
    def __init__(self,id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return 'Vehicle number : ' + self.id

def main():
    c = Car("32러5234")
    print(len(c))
    print(str(c))

main()