def deco(func):
    def df():
        print("emoticon!")
        func()
        print("emoticon!")
    return df

@deco
def smile():
    print("^_^")

smile()