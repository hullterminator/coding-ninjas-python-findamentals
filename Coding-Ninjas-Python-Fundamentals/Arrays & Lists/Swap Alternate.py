'''
Swap Alternate

You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
You don't need to print or return anything, just change in the input array itself.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
Output Format :
For each test case, print the elements of the resulting array in a single row separated by a single space.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
Time Limit: 1sec
Sample Input 1:
1
6
9 3 6 12 4 32
Sample Output 1 :
3 9 12 6 32 4
Sample Input 2:
2
9
9 3 6 12 4 32 5 11 19
4
1 2 3 4
Sample Output 2 :
3 9 12 6 32 4 11 5 19
2 1 4 3
'''

#your code goes here

def rev(li):
    l = len(li)
    if l % 2 == 0:
        for i in range(0, l, 2):
            li[i], li[i + 1] = li[i + 1], li[i]
    else:
        for i in range(0, l - 1, 2):
            li[i], li[i + 1] = li[i + 1], li[i]
    for i in li:
        print(i, end=' ')
    print()


num = int(input())
i = 0
while i < num:
    n = int(input())
    li = [int(x) for x in input().split()[:n]]
    rev(li)
    i += 1