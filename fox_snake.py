def fox_snake():
    a = input().split()
    b = ""
    j = 0
    for i in range(1,int(a[0])+1):
        if i % 2 != 0:
            b += "#"*int(a[1]) +","
        else:
            if j % 2 == 0:
                b += "."*(int(a[1])-1) + "#"+ ","
            else:
                b += "#" + "."*(int(a[1])-1)+","
            j += 1
    c = b.strip().split(",")

    print(*c, sep ="\n")

fox_snake()