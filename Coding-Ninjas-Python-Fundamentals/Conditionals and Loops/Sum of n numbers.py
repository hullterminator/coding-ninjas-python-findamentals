'''
Sum of n numbers

Given an integer n, find and print the sum of numbers from 1 to n.
Note : Use while loop only.
Input Format :
Integer n
Output Format :
Sum
Constraints :
1 <= n <= 100
Sample Input :
10
Sample Output :
55
'''
#your code goes here

# Read input as sepcified in the question
# Print output as specified in the question
n=int(input())
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)