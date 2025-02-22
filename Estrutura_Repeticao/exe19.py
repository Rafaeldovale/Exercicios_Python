'''18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

def conjunto():
    lista = []
    deseja = ' '
 
    while deseja != 'N':
        num = int(input("Digite um número: "))
        deseja = str(input('Deseja continuar [S/N]')).upper()

        while num > 1000 or num < 0:
            num = int(input("Digite um número: "))
        
        lista.append(num)
    soma = max(lista) + min(lista)    
    print(f'O maior valor foi {max(lista)} e o menor valor foi {min(lista)}')
    print(f'A soma entre eles será {soma}')

conjunto()