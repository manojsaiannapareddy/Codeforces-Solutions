def odd_divisor():
    a = int(input())
    ans = []
    for i in range(a):
        b = int(input())
        if (b != 0 and (b &(b-1)) != 0) == True:
            ans.append("YES")
        else:
            ans.append("NO")
    
    print(*ans, sep = '\n')

odd_divisor()