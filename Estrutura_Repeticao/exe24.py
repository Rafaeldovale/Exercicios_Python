def media():
    deseja = ' '
    c = soma = 0
    
    while deseja != 'N':
        num = float(input('Digite o valor da nota: '))

        deseja = str(input('deseja continuar: [S/N]')).upper()

        c += 1

        soma += num
    
    media = soma / c
    print(f'A média será {media:.1f}')

media()