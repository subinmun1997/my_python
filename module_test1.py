import module

def main():
    r = float(input("반지름 입력: "))
    ar = module.ar_circle(r)
    print("넓이: ",ar)
    ci = module.ci_circle(r)
    print("둘레: ",ci)

main()