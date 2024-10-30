import math 

def die_roll():
    Y, W = map(int, input().strip().split())
    
    max_roll = max(Y, W)
    winning_rolls = max(0, 7 - max_roll)
    total_outcomes = 6
    numerator = winning_rolls
    denominator = total_outcomes
    gcd = math.gcd(numerator, denominator)
    
    numerator //= gcd
    denominator //= gcd
    return f"{numerator}/{denominator}"

print(die_roll())