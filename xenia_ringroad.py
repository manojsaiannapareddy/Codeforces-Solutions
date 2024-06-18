def xenia_ringroad():
    a, b = map(int, input().split())
    lst = [int(x) - 1 for x in input().split()]
    x, y = 0, 0

    for i in lst:
        if i < x:
            y += a - abs(i- x)
        else:
            y += abs(i - x)
        x = i

    return y

print(xenia_ringroad())
