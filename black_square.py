def black_square():
    ans = 0
    a,b,c,d = map(int, input().split())
    dict1 = {}
    dict1["1"] = a
    dict1["2"] = b
    dict1["3"] = c
    dict1["4"] = d

    x = input()

    for i in x:
        ans += dict1[i]
    print(ans)

black_square()