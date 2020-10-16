class Simple:
    count = 0
    def __init__(self):
        Simple.count += 1
    @classmethod
    def get_count(cls):
        return cls.count # cls에 전달되는 것은 Simple 클래스

def main():
    print(Simple.get_count())
    s = Simple()
    print(Simple.get_count())

main()