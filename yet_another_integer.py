def yet_another_integer():
    a = int(input())
    ans = []
    for i in range(a):
        b, c = map(int, input().split())
        diff = abs(b - c)
        steps = diff // 10
        if diff % 10!= 0:
            steps += 1
        ans.append(steps)
    
    print(*ans, sep = "\n")

yet_another_integer()