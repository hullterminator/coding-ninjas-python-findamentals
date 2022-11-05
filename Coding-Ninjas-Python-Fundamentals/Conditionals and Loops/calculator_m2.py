n=1
while True:
    n=int(input())
    if 1<=n<=6:
        i1=int(input())
        if i1!=0:
            i2=int(input())
        if n==1:
            print(i1+i2)
        elif n==2:
            print(i1-i2)
        elif n==3:
            print(i1*i2)
        elif n==4:
            print(i1//i2)
        elif n==5:
            print(i1%i2)
        elif n == 6:
            exit()
    else:
        print('Invalid Operation')