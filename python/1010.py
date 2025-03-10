x = input().split(" ")
y = input().split(" ")

code1, unit1, price1 = x
code2, unit2, price2 = y

total = (float(price1)*int(unit1)) + (float(price2)*int(unit2))

print("VALOR A PAGAR: R$ %.2f"%total)