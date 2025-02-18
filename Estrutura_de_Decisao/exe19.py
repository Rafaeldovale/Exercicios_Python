def testar(num):

    if num < 1000:
        unidade = num % 10

        dezena = (num % 100) // 10

        centena = num // 100

        print(f'centena = {centena}, dezena = {dezena}, unidade = {unidade}')

numero = int(input('Entre com o valor, tem que ser menor que 1000: '))
testar(numero)