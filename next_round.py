def next_round():
    a = input()
    b = input()
    count = 0
    d = b.split()
    c = int(a.split()[1])
    for i in d:
        if int(i) >= int(d[c-1]) and int(i)> 0:
            count +=1 
 
    return count
 
print(next_round())