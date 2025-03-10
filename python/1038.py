import sys

data = sys.stdin.read().strip().split()
X = int(data[0])
Y = int(data[1])

prices = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

if X in prices:
    total = prices[X] * Y
    print(f"Total: R$ {total:.2f}")
