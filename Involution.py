def main():
    num = input("정수 입력: ")
    if num.isdigit():
        print(int(num)**2)
    else:
        print("정수가 아닙니다.")

main()