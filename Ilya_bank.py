def ilya_bank():
    a = int(input())
    if a >= 0:
        return a
    else:
        if int(str(a)[:-1]) > int(str(a)[:-2]+str(a)[-1]):
            return int(str(a)[:-1])
        else:
            return int(str(a)[:-2]+str(a)[-1])
        
print(ilya_bank())