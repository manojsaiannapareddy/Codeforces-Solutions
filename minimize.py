def minimize():
    a = int(input())
    ans = []
    for i in range(a):
        b,c = map(int, input().split())
        temp = (b + c)//2
        ans.append((temp-b)+(c-temp))

    print(*ans, sep = "\n")


minimize()

