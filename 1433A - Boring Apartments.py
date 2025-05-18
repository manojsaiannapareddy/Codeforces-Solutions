def boring_apartment():
    a = int(input())
    ans = []
    temp = [1, 11, 111, 1111, 2, 22, 222, 2222, 3, 33, 333, 3333, 4, 44, 444, 4444, 5, 55, 555, 5555, 6, 66, 666, 6666, 7, 77, 777, 7777, 8, 88, 888, 8888, 9, 99, 999, 9999]

    for i in range(a):
        b = int(input())
        count = 0
        for j in temp[:temp.index(b) +1]:
            count += len(str(j))

        ans.append(count)
    
    print(*ans, sep = "\n")

boring_apartment()