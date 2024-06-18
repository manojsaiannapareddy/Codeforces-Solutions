def new_year_meeting():
    a = list(map(int, input().split()))
    a = sorted(a)
    return  (a[2] - a[1]) + (a[1] - a[0])

print(new_year_meeting())