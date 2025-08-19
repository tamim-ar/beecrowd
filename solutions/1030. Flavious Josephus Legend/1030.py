def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + k - 1) % n + 1

nc = int(input())
for i in range(nc):
    n, k = map(int, input().split())
    result = josephus(n, k)
    print(f"Case {i+1}: {result}")
