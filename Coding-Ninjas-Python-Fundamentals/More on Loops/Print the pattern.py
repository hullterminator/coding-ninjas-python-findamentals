## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

if n % 2 == 0:
    m = n // 2
else:
    m = n // 2 + 1

for i in range(1, m + 1, 1):
    for j in range(1, n + 1, 1):
        print(2 * n * (i - 1) + j, end='')
        print(' ', end='')
    print()

r = n - m
for i in range(r, 0, -1):
    for j in range(1, n + 1, 1):
        print((2 * i - 1) * n + j, end='')
        print(' ', end='')
    print()