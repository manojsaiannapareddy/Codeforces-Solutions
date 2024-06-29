import math
def cheap_travel():
    n,m,a,b = map(int, input().split())
    cost_single = n * a
    cost_special = math.ceil(n/m) * b
    cost_combined = (n//m) * b + (n%m) * a

    return min(cost_single, cost_special, cost_combined)
    
    

print(cheap_travel())

