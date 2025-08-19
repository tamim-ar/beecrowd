n = int(input())

total_animals = 0
rabbits = rats = frogs = 0

for _ in range(n):
    amount, animal_type = input().split()
    amount = int(amount)
    
    total_animals += amount
    
    if animal_type == 'C':
        rabbits += amount
    elif animal_type == 'R':
        rats += amount
    elif animal_type == 'S':
        frogs += amount

print(f"Total: {total_animals} cobaias")
print(f"Total de coelhos: {rabbits}")
print(f"Total de ratos: {rats}")
print(f"Total de sapos: {frogs}")
print(f"Percentual de coelhos: {rabbits / total_animals * 100:.2f} %")
print(f"Percentual de ratos: {rats / total_animals * 100:.2f} %")
print(f"Percentual de sapos: {frogs / total_animals * 100:.2f} %")
