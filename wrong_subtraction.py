def wrong_subtraction():
    a = input().split()
    i = 0
    b = a[0]
    while i != int(a[1]):
        if int(b[-1]) != 0:
            b = str(int(b)-1)
            i += 1
        else:
            b = str(int(b)//10)
            i += 1

    return b

print(wrong_subtraction())