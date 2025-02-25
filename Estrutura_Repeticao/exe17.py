def fatorial():

    valor = int(input('Qual o valor a verificar: '))

    if valor < 0:
        print('O número deve ser positivo.')
    else: 
        fatorial = 1

        for i in range(1, valor + 1):

            fatorial *= i


        print(f'{valor}! = {fatorial}')

fatorial()