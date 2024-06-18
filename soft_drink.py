def soft_drinks():
    a = list(map(int, input().split()))
    milliliters = (a[1] * a[2])// a[6]
    c = a[3] * a[4]
    d = a[5]// a[-1]
    return min(milliliters, c, d) // a[0] 

print(soft_drinks())