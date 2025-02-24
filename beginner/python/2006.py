# Read the actual tea type
T = int(input())

# Read the contestants' answers
answers = list(map(int, input().split()))

# Count the number of correct answers
correct_count = answers.count(T)

# Print the result
print(correct_count)
