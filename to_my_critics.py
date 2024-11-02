def to_my_critics():
    a = int(input())
    ans =  []
    for i in range(a):
        x,y,z = map(int, input().split())
        if int(x) + int(y) >= 10 or int(x) + int(z) >= 10 or int(y) + int(z) >= 10:
            ans.append("YES")
        else:
            ans.append("NO")

    print(*ans, sep = "\n")


to_my_critics()