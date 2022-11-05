'''
Array Sum

Given an array of length N, you need to find and print the sum of all elements of the array.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Output Format :
Sum
Constraints :
1 <= N <= 10^6
Sample Input :
3
9 8 9
Sample Output :
26
'''

#your code goes here

## Read input as specified in the question.
## Print output as specified in the question.
# Python 3 code to find sum
# of elements in given array

n = int(input())
l = [int(x) for x in input().split()]
sum = 0
for i in l:
    sum = sum + i
print(sum)