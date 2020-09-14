def main():
    gcm=0
    n=42
    while True:
        if (42%n)==0 and (120%n)==0:
            gcm = n
            print(gcm)
            break
    n=n-1

main()