def medium_number():
    a = int(input())
    ans = []
    for i in range(a):
        b = list(map(int, input().split()))
        b = sorted(b)
        ans.append(b[1])

    print(*ans, sep = '\n')

medium_number()