while True:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    start = min(M, N)
    end = max(M, N)
    total = 0
    for i in range(start, end + 1):
        print(i, end=' ')
        total += i
    print(f"Sum={total}")
