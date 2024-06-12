def games():
    a = int(input())
    home_colors = []
    guest_colors = []

    for i in range(a):
        b = list(map(int, input().split()))
        home = b[0]
        guest = b[1]
        home_colors.append(home)
        guest_colors.append(guest)
    count = 0
    for j in range(a):
        for k in range(a):
            if  j != k and home_colors[j] == guest_colors[k]:
                count += 1

    return count

print(games())