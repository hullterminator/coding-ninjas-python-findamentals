## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

for i in range(1, n + 1, 1):
    for sp in range(1, i, 1):
        print(' ', end='')

    for j in range(i, n + 1, 1):
        print(j, end='')
        # print(' ',end ='')

    print()

for i in range(n - 1, 0, -1):
    for sp in range(1, i, 1):
        print(' ', end='')

    for j in range(i, n + 1, 1):
        print(j, end='')
        # print(' ',end ='')

    print()