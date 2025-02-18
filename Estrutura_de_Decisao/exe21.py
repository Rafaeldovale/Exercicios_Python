def caixa(n):

    if n > 10 and n < 600: 
        cem = int(n / 100)
        n = n% 100

        cinquenta = int(n/50)
        n = n % 50

        dez = int(n/10)
        n = n % 10

        cinco = int(n/5)
        n = n % 5

        um = n
    
    print(f'Notas R$100,00 = {cem}')
    print(f'Notas R$ 50,00 = {cinquenta}')
    print(f'Notas R$ 10,00 = {dez}')
    print(f'Notas R$  5,00 = {cinco}')
    print(f'Notas R$  1,00 = {um}')

numero = int(input('Valor para sacar [10-600]: '))
caixa(numero)