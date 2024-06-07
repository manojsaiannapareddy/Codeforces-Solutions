def george_dorm():
    a = int(input())
    count = 0
    for i in range(a):
        b = input().split()
        if int(b[0]) != int(b[1]) and (int(b[1])- int(b[0])) >= 2:
            count += 1

    return count

print(george_dorm())
            