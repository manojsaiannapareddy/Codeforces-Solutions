def tram():
    a = int(input())
    b = 0
    c = 0
    for i in range(a):
        d = input().strip().split()
        b += int(d[1])
        b -= int(d[0])
        if b > c:
            c = b

    return c

print(tram())
        

        