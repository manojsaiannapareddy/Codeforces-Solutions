def borze():
    a = str(input())
    b = ""
    if a[0] == ".":
        b += "0"
        a = a[1:]
    temp = ""
    for i in a:
        if len(temp) < 2:
            temp += i
        else:
            if temp == "-.":
                b += "1"
                temp = ""
            elif temp == "--":
                b += "2"
                temp = ""
    if a[0] != "." and len(a) %2 != 0 and a[-1] == ".":
        b += "."
    
    return b


print(borze())

            