fa_age=39

def up_fa_age():
    global fa_age
    fa_age+=1

def get_fa_age():
    return fa_age

def main():
    print("2019년...")
    print("아빠:",get_fa_age())
    print("2020년...")
    up_fa_age()
    print("아빠:",get_fa_age())

main()