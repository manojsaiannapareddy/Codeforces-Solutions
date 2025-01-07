def mishka_games():
    a = int(input())
    m_wins = 0
    c_wins = 0
    for i in range(a):
        m, c = map(int, input().split())
        if m > c:
            m_wins += 1
        elif m < c:
            c_wins += 1

    if m_wins > c_wins:
        return "Mishka"
    elif m_wins < c_wins:
        return "Chris"
    else:
        return "Friendship is magic!^^"
    
print(mishka_games())
