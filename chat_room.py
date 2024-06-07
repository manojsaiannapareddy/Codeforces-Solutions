def chat_room():
    a = "hello"
    b = str(input())
    j = 0


    for i in b:
        if i == a[j]:
            j += 1
            if j == len(a):
                return "YES"
            
    return "NO"

print(chat_room())