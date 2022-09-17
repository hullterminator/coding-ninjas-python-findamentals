def printTable(s, e, step):
    while s <= e:
        c = 5 * (s - 32) / 9
        print(s, "	", int(c))
        s = s + step


s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)