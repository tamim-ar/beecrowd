note = int(input())
n = int(note)
note100 = n / 100
n = n % 100
note50 = n / 50
n = n % 50
note20 = n / 20
n = n % 20
note10 = n / 10
n = n % 10
note5 = n / 5
n = n % 5
note2 = n / 2
n = n % 2
n1 = n
print(note)
print(
    "%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00"
    % (note100, note50, note20, note10, note5, note2, n1)
)