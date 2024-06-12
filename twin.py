def twin():
    a = int(input())
    b = input().split()
    c = []
    coins = 0
    d = 0
    for i in b:
        c.append(int(i))
    c = sorted(c)
    for i in range(len(c) -1, -1, -1):
        if d <= sum(c)//2:
            d += c[i]
            coins += 1
        else:
            break
    return coins

print(twin())

