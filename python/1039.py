import sys
import math

for line in sys.stdin:
    r1, x1, y1, r2, x2, y2 = map(int, line.split())
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("RICO" if r1 >= distance + r2 else "MORTO")
