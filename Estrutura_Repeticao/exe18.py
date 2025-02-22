'''18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

def conjunto():
    maior = menor = 0
    deseja = ' '
    while deseja != 'N':
        num = int(input('Informe um número: '))
        deseja = str(input('Deseja continuar: [S/N]')).upper()

        if num > maior:
            maior = num
        
        if num < menor:
            menor = num

        
    soma = menor + maior
    print(f'A soma entre eles foi {soma}')    
    print(f'O maior valor foi {maior} e o menor valor foi {menor}')

conjunto()