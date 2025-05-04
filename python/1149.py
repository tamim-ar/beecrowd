values = list(map(int, input().split()))
A = values[0]

# Find the first positive N after A
for N in values[1:]:
    if N > 0:
        break

sum = 0
for i in range(N):
    sum += A + i

print(sum)
