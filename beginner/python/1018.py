amount = int(input())
print(amount)

notes = [100, 50, 20, 10, 5, 2, 1]

for note in notes:
    count = amount
    print(f"{count} nota(s) de R$ {note},00")
    amount %= note