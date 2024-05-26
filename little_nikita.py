def nikita():
    a = int(input())
    ans = []
    for i in range(a):
        b = input().split()
        if int(b[0]) == int(b[1]):
            ans.append("YES")
        elif int(b[0]) < int(b[1]):
            ans.append("NO")
        elif int(b[0]) > int(b[1]):
            if (int(b[0])-int(b[1])) % 2 == 0:
                ans.append("YES")
            else:
                ans.append("NO")
 
    return "\n".join(ans)
 
print(nikita())