def boy_or_girl():
    a = input()
    b = ''
    for i in a:
        if i not in b:
            b += i
    if len(b) % 2 == 0:
        return 'CHAT WITH HER!'
    if len(b) % 2 != 0:
        return "IGNORE HIM!"
    
print(boy_or_girl())