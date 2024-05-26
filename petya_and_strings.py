def petya_string():
    a = input().lower()
    b = input().lower()
    c ='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(a)):
        if a[i] != b[i]:
            if int(c.index(a[i])) > int(c.index(b[i])):
                return 1
            elif int(c.index(a[i])) < int(c.index(b[i])):
                return -1
 
    return 0
 
print(petya_string())