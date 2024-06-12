def candies():
    a = int(input())
    lst = []
    ans = []
    for i in range(a):
        b = int(input())
        lst.append(b)
    for i in lst:
        if i < 2:
            ans.append(0)
        else:
            ans.append((i-1)//2)
    
    for i in ans:
        print(i)

candies()
