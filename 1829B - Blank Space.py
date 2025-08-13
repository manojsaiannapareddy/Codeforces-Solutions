def blank_space():
    t = int(input().strip())
    ans = []
    for _ in range(t):
        n = int(input().strip())
        a = []
        while len(a) < n:
            a.extend(map(int, input().strip().split()))
        max_len = 0
        current_len = 0
        for num in a:
            if num == 0:
                current_len += 1
                if current_len > max_len:
                    max_len = current_len
            else:
                current_len = 0
        ans.append(max_len)

    print(*ans, sep="\n")

blank_space()