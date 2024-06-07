def bazoka_mocha():
    a = int(input())
    ans =[]
    for i in range(a):
        b = int(input())
        c = list(map(int,input().split()))
        d = None
        for i in range(b):
            rotated = c[i:] + c[:i]
            if rotated == sorted(rotated):
                d = True
                break
        if d:
            ans.append("YES")
        else:
            ans.append("NO")
                 
    return "\n".join(ans)
    
print(bazoka_mocha())
