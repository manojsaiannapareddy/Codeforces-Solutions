def kth_divisible():
    a = int(input())
    ans = []
    for i in range(a):
        b,c = map(int, input().split())
        if b == c:
            ans.append(c+1)
            continue
        elif c < b:
            ans.append(c)
            continue
        x = c
        while True:
            new_x = c + (x//b)
            if new_x == x:
                break

            x = new_x
        
        ans.append(x)

    print(*ans, sep = "\n")
        

        
kth_divisible()
          
            