'''aça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada 
um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''
def cds(qtd):

    c = 1
    soma = 0 
    valor = []
    while c <= qtd:

        preco = float(input(f'Qual valor gasto no {c}º cd: R$ '))
        valor.append(preco)

        soma += preco

        c += 1

    media = soma / qtd
    print(f'A media dos valores da compra dos cds foi de R$ {media:.2f}')

quantidade = int(input('Qual a quantidade de cds foram comprados: '))
cds(quantidade)