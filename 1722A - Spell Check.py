def spell_check():
    a = int(input())
    ans = []

    for i in range(a):
        b = int(input())
        c = str(input())

        if b != 5:
            ans.append("NO")
            continue

        if "T" not in c:
            ans.append("No")
        elif "i" not in c:
            ans.append("NO")
        elif "m" not in c:
            ans.append("NO")
        elif "u" not in c:
            ans.append("NO")
        elif "r" not in c:
            ans.append("NO")
        else:
            ans.append("YES")

    print(*ans, sep = "\n")


spell_check()


        