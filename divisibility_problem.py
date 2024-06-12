import math
def div_prob():
    a = int(input())
    lst = []
    for i in range(a):
        b = input().split()
        d = int(b[0])
        e = math.ceil(d/int(b[1]))
        count = (int(b[1])*e) - int(b[0])

        lst.append(int(count))
    
    print(*lst, sep = "\n")

div_prob()
    