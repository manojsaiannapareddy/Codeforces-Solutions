def buy_shovel():
    a = input().split()
    for i in range(1, 10):
        b = i * int(a[0])
        if b % 10 == 0 or b % 10 == int(a[1]):
            return i
        
    return 10

print(buy_shovel())