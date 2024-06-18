def vanya_lanterns():
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    c = sorted(c)
    d = 0
    for i in range(1, a):
        d = max( d, c[i] - c[i-1])

    x = c[0]
    y = b - c[-1]
    f = max(d / 2.0, x, y)

    return f

print(vanya_lanterns())