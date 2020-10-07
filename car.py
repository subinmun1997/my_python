class Car:
    def __init__(self,id,f):
        self.id = id
        self.fuel = f
    def drive(self):
        self.fuel -= 10
    def add_fuel(self,f):
        self.fuel += f
    def show_info(self):
        print("id:",self.id)
        print("fuel:",self.fuel)

def main():
    c = Car("32러5344",0)
    c.add_fuel(100)
    c.drive()
    c.show_info()

main()