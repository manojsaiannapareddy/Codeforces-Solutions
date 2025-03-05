def love():
    a = int(input())
    ans = []
    temp = "codeforces"
    for i in range(a):
        b = str(input())
        count = 0
        
        for j in range(len(b)):
            if b[j] != temp[j]:
                count += 1

        ans.append(count)

    print(*ans, sep="\n")

love()
