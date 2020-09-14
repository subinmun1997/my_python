def main():
    n=1
    while n<100:
        n+=1
        if (n%2)==0 or (n%3)==0:
            continue
        print(n,end=' ')



main()