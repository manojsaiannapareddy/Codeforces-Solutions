def spy_detected():
    a = int(input())
    ans = []
    for i in range(a):
        b = int(input())
        c = list(map(int, input().split()))
        d = sorted(c)
        if d[0] == d[1]:
            ans.append((c.index(d[-1])) + 1)
        else:
            ans.append((c.index(d[0])) + 1)

    print(*ans, sep = "\n")

spy_detected()
