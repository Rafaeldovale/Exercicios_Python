def combustivel():
    valorAcool = 1.9
    valorGasolina = 2.5

    encher = (input('QUal tipo vai encher: [a]lcool [g]asolina ')).upper()
    qtdLitros = int(input('Qual a quantidade de litros: '))

    if encher == 'A':
        if qtdLitros <= 20:
            valor = (qtdLitros * 1.9)
            desc = valor - (valor  * 0.03)
        elif qtdLitros > 20:
            valor = (qtdLitros * 1.9)
            desc = valor - (valor  * 0.05)
        
        print(f'O valor a ser pago com o desconto será de R$ {desc}')

    elif encher == 'G':
        if qtdLitros <= 20:
            valor = (qtdLitros * 2.5)
            desc = valor - (valor  * 0.04)
        elif qtdLitros > 20:
            valor = (qtdLitros * 2.5)
            desc = valor - (valor  * 0.06)
        
        print(f'O valor a ser pago com o desconto será de R$ {desc}')
    
combustivel()