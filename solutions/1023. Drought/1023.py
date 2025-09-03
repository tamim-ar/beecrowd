import math
import sys
input = sys.stdin.readline

c = 1
first_city = True

while True:
    n = int(input())
    if n == 0:
        break

    if not first_city:
        print()
    first_city = False

    arr = [0] * 300
    total_people = 0
    total_consumption = 0

    for _ in range(n):
        a, b = map(int, input().split())
        total_people += a
        total_consumption += b
        arr[b // a] += a

    print(f"Cidade# {c}:")
    c += 1

    output = []
    for i in range(300):
        if arr[i] > 0:
            output.append(f"{arr[i]}-{i}")
    print(" ".join(output))

    avg = total_consumption / total_people
    ip = int(avg)
    fp = int((avg - ip) * 100)
    if fp < 10:
        print(f"Consumo medio: {ip}.0{fp} m3.")
    else:
        print(f"Consumo medio: {ip}.{fp} m3.")
