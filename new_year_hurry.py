def new_year_hurry():
    a ,b = map(int, input().split())
    c = 240 - b
    d = 0
    e = 0

    for i in range(1, a + 1):
        x = 5 * i
        if d + x <= c:
            d += x
            e += 1
        else:
            break

    return e

print(new_year_hurry())