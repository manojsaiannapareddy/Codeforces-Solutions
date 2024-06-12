def lottery():
    a = int(input())
    count = 0
    if a >= 100:
        count += a//100
        count += (a % 100)//20
        count += (a % 20)// 10
        count += (a % 10)// 5
        count += (a % 5)// 1
    if 20 <= a < 100:
        count += (a % 100)//20
        count += (a % 20)//10
        count += (a % 10)// 5
        count += (a % 5)// 1
    if 10 <= a < 20:
        count += (a % 20)//10
        count += (a % 10)// 5
        count += (a % 5)// 1
    if 5 <= a < 10:
        count += (a % 10)// 5
        count += (a % 5)// 1
    if 1 <= a < 5:
        count += (a % 5)// 1

    return count

print(lottery())




    
