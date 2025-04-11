# Read number of test cases
N = int(input())

# Process each test case
for _ in range(N):
    X, Y = map(int, input().split())
    
    # Ensure that X is less than Y, otherwise swap
    if X > Y:
        X, Y = Y, X
    
    # Sum the odd numbers between X and Y
    total_sum = 0
    for i in range(X + 1, Y):
        if i % 2 != 0:  # Check if the number is odd
            total_sum += i
    
    # Output the result for the current test case
    print(total_sum)
