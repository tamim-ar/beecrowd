x, y = map(int, input().split())

for i in range(1, y + 1):
    print(i, end='\n' if i % x == 0 else ' ')
