def investigacao():
    cont = 0
    caso1 = str(input('telefonou para vitima? [S/N] ')).upper()
    if caso1 == 'S':
        cont += 1
    caso2 = str(input('Esteve no local do crime? [S/N] ')).upper()
    if caso2 == 'S':
        cont += 1
    caso3 = str(input('Mora perto da vitima? [S/N] ')).upper()
    if caso3 == 'S':
        cont += 1
    caso4 = str(input('Devia para vitima? [S/N] '))
    if caso4 == 'S':
        cont += 1
    caso5 = str(input('Já trabalhou com a vitima? [S/N] ')).upper()
    if caso5 == 'S':
        cont += 1

    somaDosCasos = cont
   

    if somaDosCasos == 2:
        print('Suspeita')
    elif 3 <= somaDosCasos <= 4:
        print('Cumplice')
    elif somaDosCasos == 5:
        print('Culpado')
    else:
        print('Inocente')    
investigacao()