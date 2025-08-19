alcool = gasolina = diesel = 0

while True:
    code = int(input())
    if code == 1:
        alcool += 1
    elif code == 2:
        gasolina += 1
    elif code == 3:
        diesel += 1
    elif code == 4:
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
