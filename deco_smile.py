def smile():
    print("^_^")

def confused():
    print("@_@")

def deco(func):
    def df():
        print("emoticon!")
        func()
        print("emoticon!")
    return df

smile = deco(smile)
smile()

confused = deco(confused)
confused()