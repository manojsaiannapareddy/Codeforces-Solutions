def vanya_fence():
    a = input().strip().split()
    b = input().strip().split()
    c = 0
    for i in b:
        if int(i) > int(a[1]):
            c += 2
        else:
            c += 1

    return c

print(vanya_fence())