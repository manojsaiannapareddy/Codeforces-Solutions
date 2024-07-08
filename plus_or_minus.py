def plus_or_minus():
    a = int(input())
    ans =[]
    for i in range(a):
        x,y,z = map(int, input().split())
        if x + y == z:
            ans.append('+')
        else:
            ans.append('-')

    
    print(*ans, sep = "\n")

plus_or_minus()
        
    