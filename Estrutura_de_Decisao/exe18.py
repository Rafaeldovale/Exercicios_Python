def verificar(a, m, d):

    if len(a) < 4:
        print('Formato do ano inválido, tem que ser 4 digitos!')
    elif len(m) < 2:
        print('formato do mês inválido, tem que ser 2 digitos!')
    elif len(d) < 2:
        print('Formato do dia inválido, tem que ser 2 digitos!')
    elif int(m) > 12:
        print('Valor do mÊs excedido')
    elif int(d) > 31:
        print('Valor do dia excedido')
    else:
        print(f'{a}/{m}/{d}')
        

ano = (input('Informe o ano: '))
mes = (input('Informe o mês: '))
dia = (input('Informe o dia: '))

verificar(ano, mes, dia)