def short_sort():
    a = int(input())
    ans = []
    for i in range(a):
        b = input()
        if b[0] == "a" or b[1] == "b" or b[2] == "c":
            ans.append("YES")
        else:
            ans.append("NO")

    print(*ans, sep= "\n")
        
short_sort()
