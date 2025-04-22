def multiply():
    b = int(input())
    ans = []
    for i in range(b):
        b = int(input())
        cnt2 = 0
        cnt3 = 0
        while b % 2 == 0:
            cnt2 += 1
            b //= 2
        while b % 3 == 0:
            cnt3 += 1
            b //= 3
        if b != 1 or cnt2 > cnt3:
            ans.append(-1)
        else:
            ans.append((cnt3 - cnt2) + cnt3)

    print(*ans, sep="\n")

multiply()