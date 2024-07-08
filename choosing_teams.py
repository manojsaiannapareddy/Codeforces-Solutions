def choosing_teams():
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    team = 0
    ans = 0
    for i in c:
        if i + b <= 5:
            team += 1
        
        if team == 3:
            ans += 1
            team = 0

    return ans

print(choosing_teams())

