def soldier_bananas():
    a = input().split()
    cost = 0
    for i in range(1,int(a[2])+1):
        cost += (int(a[0]) *i)
    if cost < int(a[1]):
        return 0
    
    return cost - int(a[1])
 
print(soldier_bananas())