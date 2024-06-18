a, b = map(int, input().split())

c = min(a,b)

x = a - c
y = b - c

z = max(x,y) // 2

print(c, z)