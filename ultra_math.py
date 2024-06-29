def ultra_math():
    a = str(input())
    b = str(input())
    c = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            c += "0"
        else:
            c += "1"
    return c

print(ultra_math())
