inter_wins = gremio_wins = draws = total = 0

while True:
    inter, gremio = map(int, input().split())
    total += 1

    if inter > gremio:
        inter_wins += 1
    elif gremio > inter:
        gremio_wins += 1
    else:
        draws += 1

    print("Novo grenal (1-sim 2-nao)")
    choice = int(input())
    if choice == 2:
        break

print(f"{total} grenais")
print(f"Inter:{inter_wins}")
print(f"Gremio:{gremio_wins}")
print(f"Empates:{draws}")

if inter_wins > gremio_wins:
    print("Inter venceu mais")
elif gremio_wins > inter_wins:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
