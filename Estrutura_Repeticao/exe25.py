def media():

    deseja = []
    soma = c = 0

    while deseja != 'N':
        n = float(input('Informe a idade: '))

        c  += 1

        soma += n

        deseja = str(input('Deseja continuar: [N/S]')).upper()

    media = soma / n
    if 0 <= media <= 25:
        print('Turma jovem')

    elif 26 <= media <=60:
        print('Turma adulta')
        
    elif media > 60:
        print('Turma idosa')

media()