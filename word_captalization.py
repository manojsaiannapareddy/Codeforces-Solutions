def word_cap():
    a = input()
    b = ''
    b += a[0].upper()
    b += a[1:]
    return b
 
print(word_cap())