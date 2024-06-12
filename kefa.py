def kefa():
    a = int(input())
    b = input().split()
    max_length = 1
    d = 1
    for i in range(1, a):
        if int(b[i-1]) <= int(b[i]):
            d += 1
            if d > max_length:
                max_length = d
        if int(b[i-1]) > int(b[i]):
            d = 1
    return max_length

print(kefa())
