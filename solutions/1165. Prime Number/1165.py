import math

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    x = int(input())
    if is_prime(x):
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
