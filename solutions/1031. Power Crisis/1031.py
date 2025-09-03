def solve(N):
    def josephus(n, k):
        res = 0
        for i in range(1, n+1):
            res = (res + k) % i
        return res

    m = 1
    while True:
        if josephus(N-1, m) == 12:  
            return m
        m += 1

while True:
    N = int(input())
    if N == 0:
        break
    print(solve(N))
