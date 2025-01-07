def bit():
    n = int(input())
    x = 0
    for i in range(n):
        a = input()
        c = 0
        if '++' in a:
            x += 1
        if '--' in a:
            x -= 1
    print(x)
 
bit()