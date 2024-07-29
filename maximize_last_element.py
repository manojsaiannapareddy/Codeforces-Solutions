def maximize_last_element():
    a = int(input())
    ans = []
    for i in range(a):
        b = int(input())
        test_case = list(map(int, input().split()))
        if b == 1:
            ans.append(test_case[0])
            continue
        else:
            temp = []
            for i in range(len(test_case)):
                if i %2 == 0:
                    temp.append(test_case[i])
            
            ans.append(max(temp))

    print(*ans, sep="\n")


maximize_last_element()



