def anton_danik():
    a = int(input())
    b = input()
    an = b.count("A")
    da = b.count("D")
    if an > da:
        return "Anton"
    if da > an:
        return "Danik"
    if da == an:
        return "Friendship"
    
print(anton_danik())