def dominopiling():
    a = input()
    b = a.split()
    if int(b[0]) == 0 or int(b[1]) == 0:
        return 0
    if (int(b[0]) * int(b[1])) % 2 == 0:
        return (int(b[0]) * int(b[1]))//2
    if (int(b[0]) * int(b[1])) % 2 != 0:
        c =(int(b[0]) * int(b[1]))-1
        return c//2
print(dominopiling())