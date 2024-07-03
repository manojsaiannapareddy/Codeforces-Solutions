def lucky():
    a = int(input())
    ans = []
    for i in range(a):
        b = str(input())
        temp1 = 0
        temp2 = 0
        for i in b[0:3]:
            temp1 += int(i)
        for i in b[3:]:
            temp2 += int(i)
        if temp1 == temp2:
            ans.append("YES")
        else:
            ans.append("NO")

    
    print(*ans, sep = "\n")


lucky()