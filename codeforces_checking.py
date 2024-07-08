def codeforces_cheking():
    a = int(input())
    ans = []
    for i in range(a):
        b = str(input())
        if b in 'codeforces':
            ans.append("YES")
        else:
            ans.append("NO")

    print(*ans, sep = "\n")

codeforces_cheking()