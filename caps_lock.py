def fix_caps_lock():
    a = input()
    if len(a) == 1:
        if a.isupper():
            return a.lower()
        return a.upper()
    
    if a.isupper():
        return a.lower()
    
    if a[1:].isupper():
        return a[0].upper() + a[1:].lower()
    
    
    return a

print(fix_caps_lock())