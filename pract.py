def balanced_array():
    a = int( input())
    ans = []
    for i in range(a):
        b = int(input())
        evens = []
        for i in range(1,(b/2)+1):
            evens.append(2*1)
        odd = []
        for i in range((b/2)):
            if max(evens) - max(odd) % 2 != 0 and len(evens) - len(odd) == 1:
                odd.append(max(evens) - max(odd) )
