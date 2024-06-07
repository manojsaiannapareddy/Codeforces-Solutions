def unique(n):
    a = str(n)
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    if len(b) == len(a):
        return True
    else:
        return False
    
def beautiful_year():
    a = int(input())
    a += 1
    while not unique(a):
        a += 1
    return a
 
print(beautiful_year())