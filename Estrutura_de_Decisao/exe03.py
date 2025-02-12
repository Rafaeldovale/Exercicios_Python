def sexo(e):
    if e == 'M':
        print('M - Masculino')
    elif e == 'F':
        print('F - Feminino')
    else:
        print('Sexo inválido')

escolhe = str(input('Escolhe a opção desejada: [M] [F]')).upper()
sexo(escolhe)