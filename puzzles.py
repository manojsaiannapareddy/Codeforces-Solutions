def puzzle():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    
    min_d = float('inf')
    for i in range(m - n + 1):
        cur_d = s[i + n - 1] - s[i]
        if cur_d < min_d:
            min_d = cur_d
    
    return min_d

print(puzzle())