def division():
    a = int(input())
    ans = []
    for i in range(a):
        b = int(input())
        if b <= 1399:
            ans.append("Division 4")
        elif 1400 <= b <= 1599:
            ans.append("Division 3")
        elif 1600 <= b <= 1899:
            ans.append("Division 2")
        else:
            ans.append("Division 1")
        
    print(*ans, sep = "\n")

division()