def main():
    bread = 10
    try:
        people=int(input("몇 명? "))
        print("1인당 빵의 수: ",bread/people)
        print("맛있게 드세요.")
    except ValueError:
        print("입력이 잘못되었습니다.")
    except ZeroDivisionError:
        print("0으로는 나눌 수 없습니다.")

main()