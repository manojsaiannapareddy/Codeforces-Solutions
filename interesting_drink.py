def intersting_drink():
    a = int(input().strip())
    b = list(map(int, input().strip().split()))
    c = int(input().strip())
    d = [int(input().strip()) for _ in range(c)]
    b.sort()

    def binary_search(x, y):
        lo, hi = 0, len(x)
        while lo < hi:
            mid = (lo + hi) // 2
            if x[mid] <= y:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    results = []
    for max_price in d:
        count = binary_search(b, max_price)
        results.append(count)

    print(*results, sep = "\n")

        
intersting_drink()