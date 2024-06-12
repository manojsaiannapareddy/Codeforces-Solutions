def presents():
    a = int(input())
    b = input().split()
    givers = [0] * a  
    for i in range(a):
        givers[int(b[i]) - 1] = i + 1 
    return " ".join(map(str, givers))
print(presents())
        