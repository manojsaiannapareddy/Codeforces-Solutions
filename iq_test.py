def iq_test():
    a = int(input())
    b = list(map(int, input().split()))
    count = 1
    even = ""
    odd = ""
    if b[0] %2 == 0:
        even += str(b[0])
    elif b[0] % 2 != 0:
        odd += str(b[0])
    if b[1] %2 == 0:
        even += str(b[0])
    elif b[1] % 2 != 0:
        odd += str(b[0])
    if b[2] %2 == 0:
        even += str(b[0])
    elif b[2] % 2 != 0:
        odd += str(b[0])
    if len(even) > len(odd):
        for i in b:
            if i % 2 != 0:
                return (b.index(i)) + 1
    if len(odd) > len(even):
        for i in b:
            if i % 2 == 0:
                return (b.index(i)) + 1
            
print(iq_test())

