max_value = 0
position = 0

for i in range(1, 101):
    x = int(input())
    if x > max_value:
        max_value = x
        position = i

print(max_value)
print(position)
