values = list(map(int, input().split()))
a = values[0]

# Find the first positive value after A to use as N
for n in values[1:]:
    if n > 0:
        break

total = sum(a + i for i in range(n))
print(total)
