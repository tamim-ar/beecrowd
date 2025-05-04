def fibonacci(n):
    global calls, num
    calls += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
for _ in range(n):
    num = int(input())
    calls = -1
    result = fibonacci(num)
    print(f'fib({num}) = {calls} calls = {result}')
