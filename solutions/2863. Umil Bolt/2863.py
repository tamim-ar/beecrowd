import sys

data = sys.stdin.read().strip().split()
i = 0
while i < len(data):
    t = int(data[i])
    i += 1
    times = list(map(float, data[i:i+t]))
    i += t
    print(min(times))
