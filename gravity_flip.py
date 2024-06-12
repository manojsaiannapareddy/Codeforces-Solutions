def gravity_flip():
    a = int(input())
    b = input().split()
    c = []
    for i in b:
        c.append(int(i))
    c = sorted(c)

    print(*c)

gravity_flip()