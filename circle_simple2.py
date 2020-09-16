from module import ar_circle
from module import ci_circle

def ar_circle(rad):
    print("넓이: ",rad*rad*3.14)
def ci_circle(rad):
    print("둘레: ",rad*2*3.14)

def main():
    r = float(input("반지름 입력: "))
    ar_circle(r)
    ci_circle(r)
    sum = ar_circle(r) + ci_circle(r) #예제에서 만든 함수의 이름과 가져다 쓰려는 함수의 이름이 같다. 두 함수의 이름이
                                      #구분되지 않아 오류 발생.
    print("넓이와 둘레의 합: ",sum)

main()