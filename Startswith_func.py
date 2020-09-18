class Friend:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def set_phone(self,phone):
        self.phone = phone
    def show_info(self):
        print("이름:",self.name)
        print("전화번호:",self.phone)

def main():
    st=[]
    st.append(Friend('윤지민','010-111-222'))
    st.append(Friend('이선준','010-333-444'))
    st.append(Friend('장지우','010-555-666'))
    st.append(Friend('윤지율','010-777-888'))

    for i in st:
        if(i.get_name().startswith('윤')):
            i.show_info()

main()