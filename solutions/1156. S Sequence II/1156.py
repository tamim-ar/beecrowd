S = 0
denominator = 1
for numerator in range(1, 40, 2):
    S += numerator / denominator
    denominator *= 2
print(f"{S:.2f}")
