def remove_small():
    a = int(input())
    ans = []
    for i in range(a):
        b = int(input())
        c = list(map(int, input().split()))
        c = sorted(c)
        if len(c) == 1:
            ans.append("YES")
            continue
        possible = True
        for j in range(b - 1):
            if c[j + 1] - c[j] > 1:
                possible = False
                break
        if possible:
            ans.append("YES")
        else:
            ans.append("NO")

    print(*ans, sep="\n")

remove_small()

        
        
