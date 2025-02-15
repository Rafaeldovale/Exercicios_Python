def ano():
    
    a = int(input('Informe o ano a ser analisado: '))
    if a % 4 == 0 and a % 100 == 0:
        print('É um ano bissexto ')
    elif a % 400 == 0:
        
        print('É um ano bissexto')
    else:
        print('Não é um ano bissexto')

ano()