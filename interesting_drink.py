def intersting_drink():
    a = int(input().strip())
    b = list(map(int, input().strip().split()))
    c = int(input().strip())
    d = [int(input().strip()) for _ in range(c)]
    b.sort()

    def binary_search(prices, max_price):
        low, high = 0, len(prices)
        while low < high:
            mid = (low + high) // 2
            if prices[mid] <= max_price:
                low = mid + 1
            else:
                high = mid
        return low
    
    results = []
    for max_price in d:
        count = binary_search(b, max_price)
        results.append(count)

    print(*results, sep = "\n")

        
intersting_drink()