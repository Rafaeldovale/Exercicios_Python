def primo(x):

    p = 1

    for c in range(2, x):
        if x % c == 0:
            p = 0

    if p == 1:
        print(f'{x} é um número primo')
    else:
        print(f'{x} não é um número primo')

valor = int(input('Digite o valor: '))
primo(valor)