def drinks():
    a = int(input())
    b = input().split()
    c = 0
    for i in b:
        c += int(i)

    return c/a

print(drinks())