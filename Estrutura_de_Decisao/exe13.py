def semana():

    while True:
        dia = (input('[1]-Domingo [2]-Segunda [3]-terça [4]-quinta [5]-sexta [6]-sabado [7]-domingo: '))

        if dia == '1':
            print('Domingo')
        
        elif dia == '2':
            print('Segunda')

        elif dia == '3':
            print('Terça')

        elif dia == '4':
            print('quarta')

        elif dia == '5':
            print('Sexta')
        
        elif dia == '6':
            print('Sabado')

        else:
            print('Valor invalido')
semana()