num = int(input('Informe um numero: '))
p = 1
for c in range(2, num):
    if num % c  == 0:
        p == 0

if p == 1:
        print(f'{num} é um número primo')
else:
        print(f'{num} não é um número primo')
