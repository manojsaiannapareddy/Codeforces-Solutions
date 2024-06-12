def wanna_guy():
    a = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = b[1:]
    e = []
    for i in c:
        if i not in d:
            d.append(i)
    d = sorted(d)
    for i in range(a):
        e.append(i+1)
    print(e, d)
    for i in e:  
        if i not in d:
            return "Oh, my keybord!"
    return "I become the guy."

print(wanna_guy())
