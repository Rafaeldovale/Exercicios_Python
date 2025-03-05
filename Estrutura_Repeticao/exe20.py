def fatorial():
    deseja = 'S'
    while deseja == 'S':
        valor = int(input('Qual o valor a verificar: '))

        if valor < 0:
            print('O número deve ser positivo.')
        
        elif valor > 16:
            print('O número deve ser menor que 16')
        else: 
            fatorial = 1

            for i in range(1, valor + 1):

                fatorial *= i


            print(f'{valor}! = {fatorial}')
        
        deseja = str(input('Deseja continuar: [S]im ou [N]ão ')).upper()

fatorial()