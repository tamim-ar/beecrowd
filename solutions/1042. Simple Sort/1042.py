A, B, C = map(int, input().split())

original = [A, B, C]
sorted_values = sorted(original)

for value in sorted_values:
    print(value)

print()

for value in original:
    print(value)
