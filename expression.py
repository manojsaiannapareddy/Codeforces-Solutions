def max_expression_value():
    a = int(input())
    b = int(input())
    c = int(input())
    expressions = [
        a + b + c,
        (a + b) * c,
        a * (b + c),
        a * b * c,
        (a * b) + c,
        a + (b * c),
        (a + b) + c
    ]
    
    return max(expressions)


print(max_expression_value())