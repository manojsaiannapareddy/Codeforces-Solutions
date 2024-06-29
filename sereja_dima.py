def sereja_dima():
    a = int(input())
    b = list(map(int, input().split()))
    ans1, ans2 = 0,0
    c = 0
    for i in range(len(b)):
        if c % 2 == 0:
            ans1 += max(b[0],b[-1]) 
        else:
            ans2 += max(b[0],b[-1]) 
        b.remove(max(b[0],b[-1]))
        c += 1

    print(ans1, ans2)
sereja_dima()
