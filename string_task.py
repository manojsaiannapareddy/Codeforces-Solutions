def string_task():
    a = input().lower()
    b = '.'
 
    for i in a:
        if i not in 'aeiouy':
            b += i
            b += '.'
    return b[:len(b)-1]
 
print(string_task())
 
 