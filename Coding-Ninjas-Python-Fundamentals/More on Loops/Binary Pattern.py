## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

for i in range(1, n + 1, 1):

    for j in range(1, n - i + 2, 1):
        if (i % 2 != 0):
            print('1', end='')

        else:
            print('0', end='')

    print()