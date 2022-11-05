'''
Number Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
12345
1234
123
12
1
'''

#your code goes here

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i=1

while i <= n:
    j=1
    while j <= n-i+1:
        print(j,end ='')
        j=j+1
    print()
    i=i+1