def elephant():
    a = int(input())
    b = 0
    steps = 0
    if a > 5:
        b = a//5
        if a % 5 == 0:
            return b
        elif a % 5 != 0:
            steps +=(b + 1)
    
    else:
        return 1
    
    return steps
 
print(elephant())