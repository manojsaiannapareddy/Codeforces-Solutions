def team():
    n = int(input())
    a = 0
    for i in range(n):
        b = input()
        c = 0
        for j in range(len(b)):
            if b[j] == '1':
                c += 1
        if c >= 2:
                a += 1
 
    print(a)           
 
team()