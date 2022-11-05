## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while(i<=n) :
    s=1
    while(s<=n-i) :
        print(" ",end="")
        s=s+1
    j=1
    k=i
    while(j<=i) :
        print(k,end="")
        j=j+1
        k=k+1
    k=k-2
    m=1
    while(m<=i-1) :
        print(k,end="")
        m=m+1
        k=k-1
    print()
    i=i+1