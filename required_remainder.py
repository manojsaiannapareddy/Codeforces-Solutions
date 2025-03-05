def required_remainder():
    a = int(input())
    ans = []
    for i in range(a):
        x,y,z = map(int, input().split())
        if ((z//x)*x) + y > z:
            ans.append(((z//x)*x)-(x-y))
        else:
            ans.append(((z//x)*x)+ y)
    
    print(*ans, sep = "\n")

required_remainder()