class AgeInfo:
    def up_age(self):
        self.age+=1
    def get_age(self):
        return self.age

def main():
    fa = AgeInfo()
    mo = AgeInfo()
    me = AgeInfo()

    fa.age=39
    mo.age=35
    me.age=12

    sum = fa.get_age()+mo.get_age()+me.get_age()
    print("가족 나이 합:",sum)

    fa.up_age()
    mo.up_age()
    me.up_age()
    sum = fa.get_age()+mo.get_age()+me.get_age()
    print("1년 후의 합:",sum)

main()