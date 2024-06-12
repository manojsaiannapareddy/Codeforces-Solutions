def anton():
    a = input().strip()
    a = a[1:-1]
    if not a:
        return 0
    
    letters = a.split(", ")
    b = set(letters)
    return len(b)

print(anton())