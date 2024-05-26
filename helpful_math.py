def helpful_math():
    a = input()
    b = []
    c = sorted(a.split('+'))
    print(*c, sep = '+')
    
helpful_math()