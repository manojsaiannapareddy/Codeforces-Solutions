def odd_one_out():
    a = int(input())
    ans = []
    for i in range(a):
        b = list(map(int, input().split()))
        if b[0] == b[2]:
            ans.append(b[1])
        elif b[1] == b[2]:
            ans.append(b[0])
        else:
            ans.append(b[2])

    
    print(*ans, sep = "\n")

odd_one_out()
