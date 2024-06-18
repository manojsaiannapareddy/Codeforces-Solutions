def police_recruits():
    a = int(input())
    b = list(map(int, input().split()))
    c = 0
    ans = 0
    for i in b:
        if i == -1:
            if c > 0:
                c -= 1
            else:
                ans += 1
        else:
            c += i
    return ans

print(police_recruits())

