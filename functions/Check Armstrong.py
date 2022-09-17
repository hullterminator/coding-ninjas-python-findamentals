## Read input as specified in the question.
## Print output as specified in the question.
Number = int(input())

Sum = 0
Times = 0

Temp = Number
while Temp > 0:
    Times = Times + 1
    Temp = Temp // 10

Temp = Number
for n in range(1, Temp + 1):
    Reminder = Temp % 10
    Sum = Sum + (Reminder ** Times)
    Temp //= 10

if Number == Sum:
    print('true')
else:
    print('false')