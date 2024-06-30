def borze():
    a = str(input())
    b = ""
    temp = ""
    for i in a:
        temp += i
        if temp == ".":
            b += "0"
            temp = ""
        elif temp == "-.":
            b += "1"
            temp = ""
        elif temp == "--":
            b += "2"
            temp = ""
    
    return b


print(borze())

            