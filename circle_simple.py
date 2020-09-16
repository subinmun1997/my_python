def ar_circle(rad):
    print("넓이: ",rad*rad*3.14)
def ci_circle(rad):
    print("둘레: ",rad*2*3.14)

def main():
    r = float(input("반지름 입력: "))
    ar_circle(r)
    ci_circle(r)

main()