def dislike_of_three():
    a = int(input())
    temp = []
    ans = []
    i = 0
    tempnum = 1
    while i < 1000:
        if tempnum % 3 != 0 and str(tempnum)[-1] != '3':
            temp.append(tempnum)
            i += 1
            tempnum += 1
        elif tempnum % 3 == 0 or str(tempnum)[-1] == '3':
            tempnum += 1
    for i in range(a):
        b = int(input())
        ans.append(temp[b-1])

    print(*ans, sep = '\n')

dislike_of_three()


