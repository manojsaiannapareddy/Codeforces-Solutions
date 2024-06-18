def restore_3():
    a = list(map(int, input().split()))
    b = max(a)
    ans = []
    for i in a:
        if b - i == 0:
            continue
        else:
            ans.append(b-i)

    print(*ans, sep = " ")

restore_3()