## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces+=1
    p=1
    while p<=i:
        print('*',end='')
        p+=1
    q=1
    while q<=i-1:
        print('*',end='')
        q+=1
    print()
    i+=1