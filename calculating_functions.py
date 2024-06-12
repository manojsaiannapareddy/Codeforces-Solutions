import math

def calculate_function():
    a = int(input())
    if a % 2 == 0:
        return a //2
    else:
        return math.floor(-a/2)
    
print(calculate_function())
