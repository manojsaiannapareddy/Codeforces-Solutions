import math
 
def theatresquare():
    a = input()
    b = a.split()
    if int(b[2])*int(b[2]) >= int(b[0]) *int(b[1]):
        return 1
    return math.ceil(int(b[0])/int(b[2])) * math.ceil(int(b[1])/int(b[2]))
 
print(theatresquare())