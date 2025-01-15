def stair_peak_neither():
    a = int(input())
    ans = []
    for i in range(a):
        x,y,z = map(int, input().split())
        if x < y and y < z:
            ans.append("STAIR")
        elif x < y and y > z:
            ans.append("PEAK")
        else:
            ans.append("NONE")

    print(*ans, sep = "\n")

stair_peak_neither()