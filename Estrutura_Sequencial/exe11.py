'''11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a) o produto do dobro do primeiro com metade do segundo .
    b) a soma do triplo do primeiro com o terceiro.
    c) o terceiro elevado ao cubo.'''


def cal(a, b, r):
    primeiro = (a * a) + (b / 2)
    segundo = (a * 3) + (r)
    terceiro = r ** 3

    print(f'Resposta a) {primeiro:.2f} '
          f'Resposta b) {segundo:.2f} '
          f'Resposta c) {terceiro:.2f}')

int_a = int(input('Informe um número inteiro: '))
int_b = int(input('Informe o segundo número inteiro: '))
real = float(input('Informe um número real: '))

cal(int_a, int_b, real)