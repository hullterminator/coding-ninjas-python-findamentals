## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces <=n-i:
        print(' ',end='')
        spaces+=1
    p=1
    while p<=i:
        print(p,end='')
        p+=1
    print('')
    i+=1