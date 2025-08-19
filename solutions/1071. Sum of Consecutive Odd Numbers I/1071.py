x = int(input())
y = int(input())

if x > y:
    x, y = y, x

sum_odd = sum(n for n in range(x + 1, y) if n % 2 != 0)

print(sum_odd)
