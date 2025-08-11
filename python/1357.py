while True:
    n = int(input())
    if n == 0:
        break
    score_a, score_b = 0, 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            score_a += 1
        elif b > a:
            score_b += 1
    print(score_a, score_b)
