# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def dobro():

    a = float(input('Informe a altura da área: '))
    l = float(input('Informe o comprimento da área: '))


    area = a * l

    print(f'O valor da área será de {area:.1f} e o dobro dele será de {area * 2:.1f}')

dobro()