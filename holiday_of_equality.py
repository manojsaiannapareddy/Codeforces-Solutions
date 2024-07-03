def holiday_equality():
    a = int(input())
    b = list(map(int, input().split()))
    highest = max(b)
    ans = []
    for i in  b:
        if i < highest:
            ans.append(highest - i)
    
    return sum(ans)

print(holiday_equality())