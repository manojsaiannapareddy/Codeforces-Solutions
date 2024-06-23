def game_with_sticks():
    a, b = map(int, input().split())
    if min(a,b) % 2 == 1:
        return "Akshat"
    else:
        return "Malvika"
    

print(game_with_sticks())