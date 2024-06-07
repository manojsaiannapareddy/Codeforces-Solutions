def is_lucky(num):
    for digit in str(num):
        if digit != '4' and digit != '7':
            return False
    return True

def is_nearly_lucky_number():
    count = 0
    n = input().strip()
    for digit in str(n):
        if digit == '4' or digit == '7':
            count += 1

    if is_lucky(count):
        return "YES"
    else:
        return "NO"

print(is_nearly_lucky_number())