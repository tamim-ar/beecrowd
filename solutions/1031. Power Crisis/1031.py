def solve(n):
    m = 1
    while True:
        pos = 0
        for i in range(2, n):   # simulate elimination of (n-1) regions after removing region 1 first
            pos = (pos + m) % i
        if pos == 11:  # Wellington (13) should be last → index 12 overall, but after removing region 1 it's 11
            return m
        m += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(solve(n))
