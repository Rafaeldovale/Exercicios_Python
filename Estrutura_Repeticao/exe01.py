num = 0

while True:
    num = int(input('Informe um valor de 0 até 10: '))

    if 0 <= num <= 10:
        break
    else:
        print('Valor inválido')