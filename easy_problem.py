def easy_problem():
    a = int(input())
    b = input().split()
    for i in b:
        if i == "1":
            return "HARD"
        
    return "EASY"

print(easy_problem())