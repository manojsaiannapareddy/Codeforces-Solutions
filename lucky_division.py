def is_lucky(num):
    for digit in str(num):
        if digit != '4' and digit != '7':
            return False
    return True

def is_nearly_lucky_number():
    n = int(input())
    for i in range(1, n + 1):
        if is_lucky(i) and n % i == 0:
            return "YES"
    return "NO"

print(is_nearly_lucky_number())
