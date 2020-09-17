fa_age=39

def up_fa_age():
    global fa_age
    fa_age+=1
def get_fa_age():
    return fa_age

mo_age=35

def up_mo_age():
    global mo_age
    mo_age+=1
def get_mo_age():
    return mo_age

def main():
    print("2019년...")
    print("아빠:",get_fa_age())
    print("엄마:",get_mo_age())
    print("2020년...")
    up_fa_age()
    up_mo_age()
    print("아빠:",get_fa_age())
    print("엄마:",get_mo_age())

main()