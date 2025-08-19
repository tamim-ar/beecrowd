nums = [int(input()) for _ in range(5)]

even_count = sum(1 for n in nums if n % 2 == 0)
odd_count = sum(1 for n in nums if n % 2 != 0)
positive_count = sum(1 for n in nums if n > 0)
negative_count = sum(1 for n in nums if n < 0)

print(f"{even_count} valor(es) par(es)")
print(f"{odd_count} valor(es) impar(es)")
print(f"{positive_count} valor(es) positivo(s)")
print(f"{negative_count} valor(es) negativo(s)")
