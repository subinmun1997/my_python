class AgeInfo:
    def up_age(self):
        self.age+=1
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age

def main():
    fa = AgeInfo()
    fa.set_age(39)
    fa.up_age()
    print("1년 후 아빠 나이: ",fa.get_age())

main()