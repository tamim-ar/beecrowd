valid_scores = []

while len(valid_scores) < 2:
    score = float(input())
    if 0 <= score <= 10:
        valid_scores.append(score)
    else:
        print("nota invalida")

average = sum(valid_scores) / 2
print(f"media = {average:.2f}")
