expr = input().strip()

if '+' in expr:
    a, b = expr.split('+')
    print(int(a) + int(b))
elif '-' in expr:
    a, b = expr.split('-')
    print(int(a) - int(b))
elif '*' in expr:
    a, b = expr.split('*')
    print(int(a) * int(b))
elif '/' in expr:
    a, b = expr.split('/')
    print(int(a) // int(b))   # integer division as required
