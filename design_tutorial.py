def is_composite(num):
    if num <= 1:
        return False
    if num <= 3:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return True
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i +2) == 0:
            return True
        i += 6
    
    return False

def find_composite_pair(n):
    for i in range(4, n):
        if is_composite(i):
            y = n - i
            if is_composite(y):
                return i, y
            

n = int(input())
ans1, ans2 = find_composite_pair(n)
print(ans1, ans2)