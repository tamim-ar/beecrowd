def banknotes_and_coins(n):
    values = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    labels = [
        "nota(s) de R$",
        "nota(s) de R$",
        "nota(s) de R$",
        "nota(s) de R$",
        "nota(s) de R$",
        "nota(s) de R$",
        "moeda(s) de R$",
        "moeda(s) de R$",
        "moeda(s) de R$",
        "moeda(s) de R$",
        "moeda(s) de R$",
        "moeda(s) de R$",
    ]

    n = int(round(n * 100))
    print("NOTAS:")
    for i, v in enumerate(values[:6]):
        print(f"{n // v} {labels[i]} {v / 100:.2f}")
        n %= v
    print("MOEDAS:")
    for i, v in enumerate(values[6:]):
        print(f"{n // v} {labels[i+6]} {v / 100:.2f}")
        n %= v


banknotes_and_coins(float(input()))
