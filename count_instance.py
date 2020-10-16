class Simple:
    count = 0 # Simple의 클래스 변수
    def __init__(self):
        Simple.count += 1
    def get_count(self):
        return Simple.count

def main():
    s1 = Simple()
    print(s1.get_count())
    s2 = Simple()
    print(s1.get_count())
    s3 = Simple()
    print(s2.get_count())

main()