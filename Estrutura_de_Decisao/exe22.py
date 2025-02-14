def descobrir(n):
    
    if n % 2 == 0:
        print(f'O número {n} é par')
    else:
        print(f'O número {n} é ímpar')

num = int(input('Digite um número qualquer para saber se é par ou ímpar: '))
descobrir(num)