def conversao(n):
    converte = n * 100
    return converte

a = int(input('Qua o valor em metros(m): '))

resultado = conversao(a)

print(f'{resultado} cm')