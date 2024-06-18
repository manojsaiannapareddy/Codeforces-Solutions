def love_username():
    a = int(input())
    b = list(map(int, input().split()))
    if a == 1:
        return 0
    
    highest = b [0]
    lowest = b[0]
    count = 0

    for i in range(1, a):
        if b[i] > highest:
            count += 1
            highest = b[i]
        elif b[i] < lowest:
            count += 1
            lowest = b[i]

    return count

print(love_username())