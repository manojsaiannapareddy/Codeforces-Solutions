def beautiful_matrix():
    a1 = input().split()
    a2 = input().split()
    a3 = input().split()
    a4 = input().split()
    a5 = input().split()
    b = 0
    c = 0
    if '1' in a1:
        b = abs((int(a1.index('1'))+1)-3)
        c = 2
    elif '1' in a2:
        b = abs((int(a2.index('1'))+1)-3)
        c = 1
    elif '1' in a3:
        b = abs((int(a3.index('1'))+1)-3)
        c = 0
    elif '1' in a4:
        b = abs((int(a4.index('1'))+1)-3)
        c = 1
    else:
        b = abs((int(a5.index('1'))+1)-3)
        c =2
 
    return b+c
 
print(beautiful_matrix()) 
        
        