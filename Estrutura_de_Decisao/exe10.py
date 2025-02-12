def escolha():
    op = input('Em qual turno você estuda:\n'
               'M - Matutino\n'
               'V - Vespertino\n'
               'N - Noturno: ').upper()
    if op == 'M':
        print('Bom dia')
    elif op == 'V':
        print('Boa tarde')
    elif op == 'N':
        print('Boa noite')
    else:
        print('Invalido')

escolha()