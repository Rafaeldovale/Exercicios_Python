'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma 
    função de arredondamento.'''

def descobrir(n):
    if n // 1 == n:
        print('É inteiro')
    else:
        print('É decimal')

num = float(input('Informe um número qualquer para descobrir se ele é inteiro ou decimal: '))
descobrir(num)