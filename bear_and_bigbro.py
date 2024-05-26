def bear_brothers():
    a = input().split()
    lim = int(a[0])
    big_bro = int(a[1])
    
    i = 0
    while lim <= big_bro:
        lim *= 3
        big_bro *= 2
        i += 1
 
    return i
 
print(bear_brothers())