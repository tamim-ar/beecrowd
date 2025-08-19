n = int(input())

for _ in range(n):
    a, b, c = map(float, input().split())
    weighted_avg = (a * 2 + b * 3 + c * 5) / 10
    print(f"{weighted_avg:.1f}")
