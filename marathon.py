def marathon():
    a = int(input())
    ans = []
    for i in range(a):
        b = list(map(int, input().split()))
        c = 0
        timur = b[0]
        if b[1] > timur:
            c += 1
        if b[2] > timur:
            c += 1
        if b[3] > timur:
            c += 1
        
        ans.append(c)

    print(*ans, sep = "\n")

marathon()
