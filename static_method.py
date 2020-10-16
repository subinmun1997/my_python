class Simple:
    def sm():
        print('static method!')
    sm = staticmethod(sm)

def main():
    Simple.sm()
    s = Simple()
    s.sm()

main()