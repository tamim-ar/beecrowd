N = [int(input()) for _ in range(20)]

for i in range(10):
    N[i], N[19 - i] = N[19 - i], N[i]

for i in range(20):
    print(f"N[{i}] = {N[i]}")
