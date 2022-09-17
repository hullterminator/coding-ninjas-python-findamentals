'''Find average Marks

Write a program to input marks of three tests of a student (all integers). Then calculate and print the average of all test marks.
Input format :
3 Test marks (in different lines)
Output format :
Average
Sample Input 1 :
3
4
6
Sample Output 1 :
4.333333333333333
Sample Input 2 :
5
10
5
Sample Output 2 :
6.666666666666667'''


#code goes here
# Read input as sepcified in the question
# Print output as specified in the question
#inputs
s1=int(input())
s2=int(input())
s3=int(input())
#average
avg=(s1+s2+s3)/3

print(avg)