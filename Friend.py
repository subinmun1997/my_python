class Friend:
    def __init__(self,name,tel):
        self.name = name
        self.tel = tel
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.tel
    def set_phone(self,tel):
        self.tel = tel
    def show_info(self):
        print("이름:",self.name)
        print("전화번호:",self.tel)

def main():
    f = Friend('윤성우','010-111-222')
    print(f.get_name())
    print(f.get_phone())
    print(f.set_phone('010-333-444'))
    f.show_info()

main()