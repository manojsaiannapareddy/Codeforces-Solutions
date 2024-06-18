def registration():
    a = int(input())
    b = []
    e = {}
    for i in range(a):
        c = str(input())
        if c not in e:
            b.append("OK")
            e[c] = 1
        else:
            b.append(c+ str(e[c]))
            e[c] += 1

    
    print(*b, sep = "\n")

registration()