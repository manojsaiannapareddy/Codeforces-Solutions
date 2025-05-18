def square_string():
    a = int(input())
    ans = []

    for i in range(a):
        b = str(input())

        if len(b) %2 != 0:
            ans.append("NO")
        
        else:
            if b[:len(b)//2] == b[len(b)//2:]:
                ans.append("YES")
            else:
                ans.append("NO")

    print(*ans, sep = "\n")

square_string()