def vanya_cube():
    a = int(input())
    if a ==1:
        return 1
    ans = 0
    total = 0
    count = 0
    sum_cube = 0
    while sum_cube < a:
        if total == 0:
            total += 1
            count +=1
        else:
            total += count+1
            count +=1
        sum_cube += total
    if sum_cube == a:
        ans = count
    else:
        ans = count-1

    return ans

print(vanya_cube())