def cut_ribbon():
    n,a,b,c = map(int, input().split())

    x = [-1] *(n+1)
    x[0] = 0

    for i in range(1, n + 1):
        if i >= a and x[i - a] != -1:
            x[i] = max(x[i], x[i - a] + 1)
        if i >= b and x[i - b] != -1:
            x[i] = max(x[i], x[i - b] + 1)
        if i >= c and x[i - c] != -1:
            x[i] = max(x[i], x[i - c] + 1)

    return x[n]

print(cut_ribbon())