def football():
    a = input().strip()
    if "0000000" in a or "1111111" in a:
        return "YES"
    else:
        return "NO"
print(football())
    