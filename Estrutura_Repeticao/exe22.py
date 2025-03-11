def primo(x):

    for c in range(1, x + 1):
        if x % c == 1:
            print('\033[34m', end=' ')
        else:
            print('\033[33m', end=' ')
        print(f'{c}', end='')
    
    

valor = int(input('Digite o valor: '))
primo(valor)