def even_array():
    a = int(input())
    ans = []
    for i in range(a):
        b = int(input())
        c = list(map(int, input().split()))
        temp = []
        index = 0
        even = 0
        odd = 0
        for i in c:
            if index % 2 != i % 2:
                temp.append(i)
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            index += 1
        if len(temp) % 2 == 0 and even == odd:
            ans.append(len(temp) // 2)
        
        else:
            ans.append(-1)
    
    print(*ans, sep="\n")

even_array()