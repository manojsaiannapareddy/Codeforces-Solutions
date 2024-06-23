def yes():
    a = int(input())
    ans = []
    for i in range(a):
        b= str(input()).lower()
        if b == "yes":
            ans.append("YES")
        else:
            ans.append("NO")

    print(*ans, sep = "\n")

yes()