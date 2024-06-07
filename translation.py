def translation():
    a = input()
    b = input()
    c = b[::-1]
    if c == a:
        return "YES"
    else:
        return "NO"
print(translation())