def round_numbers():
    a = int(input())
    lst1 = []
    lst2 = []
    for i in range(a):
        b = str(input())
        lst = []
        c = len(b)
        d = 0
        for i in b:
            if i != "0":
                c -= 1
                d += 1
                e = i + "0"*c
                lst.append(e)
            else:
                c -= 1
        lst1.append(d)
        lst2.append(lst)
    for i in range(len(lst1)):
        print(lst1[i])
        print(" ".join(lst2[i]))

round_numbers()