def main():
    lcm=0
    r=45
    while True:
        if (r%6)==0 and (r%45)==0:
            lcm = r
            print(lcm)
            break
        r+=1
main()