def sum():
    a = int(input())
    ans = []
    for i in range(a):
        b = list(map(int, input().split()))
        if b[0] == b[1] + b[2]:
            ans.append("YES")
        elif b[1] == b[0] + b[2]:
            ans.append("YES")
        elif b[2] == b[0] + b[1]:
            ans.append("YES")
        else:
            ans.append("NO")

    print(*ans, sep = "\n")

sum()