def arr_coloring():
    a = int(input())
    ans = []

    for i in range(a):
        b = int(input())
        c = list(map(int, input().split()))
        if sum(c) % 2 == 0:
            ans.append("YES")
        
        else:
            ans.append("NO")

    print(*ans, sep="\n")