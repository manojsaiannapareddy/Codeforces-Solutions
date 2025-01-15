def panoramixs_prediction():
    a, b = map(int, input().split())

    while True:
        a += 1
        if a > b:
            return "NO"
        for i in range(2,(a//2) +1):
            if a % i == 0:
                break
        else:  
            if a == b:
                return "YES"
            break

    return "NO"
        

            

print(panoramixs_prediction())