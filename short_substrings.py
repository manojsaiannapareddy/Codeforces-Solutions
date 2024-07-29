def short_substring():
    a = int(input())
    ans = []
    for i in range(a):
        b = str(input())
        a = b[0]
        for i in range(1,len(b),2):
            a += b[i]
        ans.append(a)

    print(*ans, sep = '\n')


short_substring()