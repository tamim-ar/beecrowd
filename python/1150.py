x = int(input())
while True:
    z = int(input())
    if z > x:
        break

total = 0
count = 0
current = x

while total <= z:
    total += current
    current += 1
    count += 1

print(count)
