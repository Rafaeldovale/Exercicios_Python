'''Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
    Exemplo:
    12376489
    => 98467321'''

def conversor(n):

        n = n[::-1]
        print(n)


num = (input('Informe o numero inteiro: '))
conversor(num)