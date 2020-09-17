class AgeInfo:
    def up_age(self):
        self.age+=1
    def get_age(self):
        return self.age

def main():
    fa = AgeInfo()
    fa.age=39

    print("현재 아빠 나이...")
    print("아빠:",fa.get_age())

    print("1년 뒤...")
    fa.up_age()
    print("아빠:",fa.get_age())

main()