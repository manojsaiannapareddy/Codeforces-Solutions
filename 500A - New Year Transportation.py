def transportation():
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    count = 1
    while count < a:
        if count == b:
            return "YES"
        
        count = count + c[count - 1]
        
        if count > a:
            return "NO"

    return "NO" if count != b else "YES"

print(transportation())