import math

def even_odd():
    a = input().split()
    if int(a[1]) <= math.ceil(int(a[0])/2):
        return 1 +(2 *(int(a[1])-1))
    else:
        return 2 * (int(a[1])- math.ceil(int(a[0])/2))
    
print(even_odd())
