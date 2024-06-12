def pangram():
    c = int(input())
    a = str(input()).lower()
    b = "abcdefghijklmnopqrstuvwxyz"
    for i in b:
        if i not in a:
            return "NO"
    return "YES"
print(pangram())