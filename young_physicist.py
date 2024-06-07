def young_physicist():
    a = int(input())
    b = 0
    c = 0
    d = 0
    for i in range(a):
        e = input().split()
        b += int(e[0])
        c += int(e[1])
        d += int(e[2])

    if b ==0 and c == 0 and d == 0:
        return "YES"
    else:
        return "NO"        
    
print(young_physicist())
