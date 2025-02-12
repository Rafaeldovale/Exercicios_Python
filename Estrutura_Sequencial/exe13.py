def peso_ideal():

    altura = float(input('Informe a altura para a analise: '))

    homem = (72.7 * altura) - 58
    mulher = (62.1 * altura) - 44.7

    print(f'O peso ideal para a altura de {altura}m para homens é de {homem:.3f} e para as mulheres é de {mulher:.3f}')

peso_ideal()