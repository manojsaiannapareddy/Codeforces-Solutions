def team_olympiad():
    a = int(input())
    b = list(map(int, input().split()))
    programming = []
    maths = []
    pt = []

    for i in range(a):
        if b[i] == 1:
            programming.append(i +1)
        elif b[i] == 2:
            maths.append(i + 1)
        elif b[i] == 3:
            pt.append(i+1)

    w = min(len(programming), len(maths), len(pt))
    print(w)

    for i in range(w):
        print(programming[i], maths[i], pt[i])

team_olympiad()