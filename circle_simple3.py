from module import ar_circle as ac
from module import ci_circle as cc

def ar_circle(rad):
    print("넓이: ",rad*rad*3.14)
def ci_circle(rad):
    print("둘레: ",rad*2*3.14)

def main():
    r = float(input("반지름 입력: "))
    ar_circle(r)
    ci_circle(r)
    sum = ac(r) + cc(r)
    print("넓이와 둘레의 합: ", sum)

main()