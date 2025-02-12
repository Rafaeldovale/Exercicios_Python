'''Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
    Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''


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