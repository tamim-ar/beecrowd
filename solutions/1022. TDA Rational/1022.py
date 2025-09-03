from math import gcd

n = int(input())

for _ in range(n):
    a, _, b, op, c, _, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if op == '+':
        num = a*d + c*b
        den = b*d
    elif op == '-':
        num = a*d - c*b
        den = b*d
    elif op == '*':
        num = a*c
        den = b*d
    elif op == '/':
        num = a*d
        den = b*c

    g = gcd(abs(num), abs(den))
    simplified_num = num // g
    simplified_den = den // g

    print(f"{num}/{den} = {simplified_num}/{simplified_den}")
