def fence():
    a, b = map(int, input().split())
    heights = list(map(int, input().split()))

    curr_sum = sum(heights[:b])
    min_sum = curr_sum
    ans = 0
    for i in range(1, a - b + 1):
        curr_sum = curr_sum - heights[i - 1] + heights[i + b - 1]
        if curr_sum < min_sum:
            min_sum = curr_sum
            ans = i

    return ans + 1 

print(fence())