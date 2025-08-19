ages = []
while True:
    n = int(input())
    if n < 0:
        break
    ages.append(n)

avg = sum(ages) / len(ages)
print(f"{avg:.2f}")
