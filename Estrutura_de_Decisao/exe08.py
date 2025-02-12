"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é 
    sempre pelo mais barato."""

def produtos(p1, p2, p3):

    if p1 <= p2  and p1 <= p3:
        print(f'VocÊ deve comprar o produto R$ {p1}')

    elif p2 <= p3 and p2 <= p1: 
        print(f'VocÊ deve comprar o produto R$ {p2}')

    elif p3 <= p2 and p3 <= p1:
        print(f'VocÊ deve comprar o produto R$ {p3}')
    
prod1 = float(input('Digite o valor do primeiro produto: R$ '))
prod2 = float(input('Digite o valor do segundo produto: R$ '))
prod3 = float(input('Digite o valor do terceiro produto: R$ '))


produtos(prod1, prod2, prod3)