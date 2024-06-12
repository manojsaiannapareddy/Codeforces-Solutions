import math
def taxi():
    a = int(input())
    b = list(map(int, input().split()))
    one = 0
    two = 0
    three = 0
    four = 0
    for i in b:
        if i == 1:
            one += 1
        elif i == 2:
            two += 2
        elif i == 3:
            three += 1
        elif i == 4:
            four += 1
    if two % 4 != 0:
        if one - 2 >= 0:
            one -= 2
        else:
            one = 0
    if one - three >= 0:
        one -= three
    else:
        one = 0

    return four + three + math.ceil(two/4) + math.ceil(one/4)

print(taxi())