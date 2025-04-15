while True:
    valid_scores = []

    while len(valid_scores) < 2:
        score = float(input())
        if 0 <= score <= 10:
            valid_scores.append(score)
        else:
            print("nota invalida")

    avg = sum(valid_scores) / 2
    print(f"media = {avg:.2f}")

    while True:
        print("novo calculo (1-sim 2-nao)")
        option = int(input())
        if option == 1 or option == 2:
            break

    if option == 2:
        break
