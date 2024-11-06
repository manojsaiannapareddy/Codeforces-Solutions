def balanced_array():
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        n = int(input().strip())
        if n % 4 != 0:
            results.append("NO")
        else:
            results.append("YES")
            even_part = [2 * i for i in range(1, n // 2 + 1)]
            odd_part = [2 * i - 1 for i in range(1, n // 2)]
            last_odd = sum(even_part) - sum(odd_part)
            odd_part.append(last_odd)
            results.append(" ".join(map(str, even_part + odd_part)))
    
    print(*results, sep="\n")

balanced_array()
