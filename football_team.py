def find_winning_team():
    goal_count = {}
    a = int(input())

    for i in range(a):
        b = input()
        if b in goal_count:
            goal_count[b] += 1
        else:
            goal_count[b] = 1

    # Determine the team with the most goals
    winning_team = max(goal_count, key=goal_count.get)
    return winning_team

print(find_winning_team())

