def way_too_long():
    n = int(input())
    abc = []
    for i in range(n):
        abc.append(str(input()))
    for i in abc:
        if len(i) <= 10:
            print(i)
        else:
            s=''
            s+=i[0]
            count = 0
            for j in i:
                count += 1
            count -= 2
            s+=str(count)
            s+=i[-1]
            print(s)
                
way_too_long()