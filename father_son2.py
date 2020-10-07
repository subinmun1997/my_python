class Father:
    def run(self):
        print("so fast, dad style")

class Son(Father):
    def run(self): #overriding
        print("so fast, son style")

def main():
    s = Son()
    s.run()

main()