def amusing_joke():
    a = str(input())
    b = str(input())
    c = str(input())
    d = {}
    count = {}
    if len(a) + len(b) != len(c):
        return "NO"
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in b:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in c:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for i in count:
        if i not in d or d[i] != count[i]:
            return "NO"
    return "YES"

print(amusing_joke())