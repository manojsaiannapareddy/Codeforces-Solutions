def hulk():
    a = int(input())
    b = ""
    count = 0
    while count < a:
        if count % 2 == 0:
            b += "I hate "
            if count != (a-1):
                b += "that "
        
        if count % 2 != 0:
            b += "I love "
            if count != (a-1):
                b += "that "
        count += 1

    b += "it"

    return b

print(hulk())