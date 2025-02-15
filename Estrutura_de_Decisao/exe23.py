def descobrir(n):
    if n // 1 == n:
        print('É inteiro')
    else:
        print('É decimal')

num = float(input('Informe um número qualquer para descobrir se ele é inteiro ou decimal: '))
descobrir(num)