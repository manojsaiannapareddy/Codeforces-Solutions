def word():
    a = input()
    b = 0
    c = 0
    for i in a:
        if i == i.lower():
            b += 1
        if i == i.upper():
            c += 1
    
    if c > b:
        return a.upper()
    else:
        return a.lower()
    
print(word())