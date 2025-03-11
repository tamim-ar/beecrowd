def fibonacci_calls(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return (0, 0)
    if n == 1:
        return (1, 0)
    
    f1, c1 = fibonacci_calls(n - 1, memo)
    f2, c2 = fibonacci_calls(n - 2, memo)
    
    memo[n] = (f1 + f2, c1 + c2 + 2)
    return memo[n]

t = int(input())
for _ in range(t):
    x = int(input())
    result, calls = fibonacci_calls(x)
    print(f"fib({x}) = {calls} calls = {result}")
