def sale():
    a,b = map(int, input().split())
    c = list(map(int, input().split()))
    c = sorted(c)
    ans = 0
    count = 0
    while count < b and c[count] < 0:
        ans += abs(c[count])
        count += 1

    return ans


print(sale())