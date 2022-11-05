## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
p=n
while i<=n:
    j=1
    while j<=n-i+1:
        print(p,end='')
        j+=1
    print()
    p-=1
    i+=1