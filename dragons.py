def dragon():
    a = input().split()
    base = int(a[0])
    n = int(a[1])
    
    levl = []
    
    for i in range(n):
        b = input().split()
        x = int(b[0])
        y = int(b[1])
        levl.append((x, y))
    levl.sort()
    
    for dragon_strength, bonus in levl:
        if base > dragon_strength:
            base += bonus
        else:
            return "NO"
    
    return "YES"

print(dragon())