def max_gcd():
    a = int(input())
    ans = []

    for i in range(a):
        b = int(input())
        ans.append(b//2)

    print(*ans, sep="\n")

max_gcd()