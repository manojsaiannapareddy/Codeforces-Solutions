def books():
    count = 0
    a,b = map(int, input().split())
    temp = list(map(int,input().split()))
    max_books = 0
    current_time = 0
    left = 0

    for right in range(a):
        current_time += temp[right] 
        while current_time > b:
            current_time -= temp[left]
            left += 1
        max_books = max(max_books, right - left + 1)

    return max_books



print(books())