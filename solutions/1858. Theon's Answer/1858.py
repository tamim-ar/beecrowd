import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
t = data[1:1+n]
print(t.index(min(t)) + 1)
