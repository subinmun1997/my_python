from module import ar_circle
from module import ci_circle

def main():
    r = float(input("반지름 입력: "))
    ar = ar_circle(r)
    print("넓이: ",ar)
    ci = ci_circle(r)
    print("둘레: ",ci)

main()