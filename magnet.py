def magnet():
    a = int(input())
    count = 0
    cur = None
    for i in range(a):
        b = int(input())
        if cur == None:
            cur = f'{b}'
            count += 1
        elif str(b) != cur:
            count += 1
            cur = f'{b}'

    return count

print(magnet())

