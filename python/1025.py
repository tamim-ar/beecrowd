import sys

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            while mid > 0 and arr[mid - 1] == x:
                mid -= 1
            return mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

case_num = 1
while True:
    n, q = map(int, sys.stdin.readline().split())
    if n == 0 and q == 0:
        break
    
    numbers = sorted(int(sys.stdin.readline()) for _ in range(n))
    queries = [int(sys.stdin.readline()) for _ in range(q)]

    print(f"CASE# {case_num}:")
    for query in queries:
        pos = binary_search(numbers, query)
        if pos != -1:
            print(f"{query} found at {pos}")
        else:
            print(f"{query} not found")
    
    case_num += 1
