def opcao():
    saldo_Inicial = 1000

    while True:

        op = input('Caixa Eletrônico\n'
                    '1 - Verificar Saldo\n'
                    '2 - Depositar Dinheiro\n'
                    '3 - Sacar Dinheir0\n'
                    '4 - Sair\n\n'
                    'Escolha uma opção (1-4): \n')
    
        if op == '1':
            
            print(f'Seu saldo é: R$ {saldo_Inicial:.2f}\n')

        elif op == '2':

            deposito = float(input('Digite o valor do depósito: R$ '))

            if deposito > 0 :
                saldo_Inicial += deposito
            
            else: 
                print(f'Valor de depósito inválido!\n')


            print(f'Depósito realizado com Sucesso!!! R$ {deposito:.2f}\n')

        elif op == '3':

            saque = float(input('Digite o valor do Saque: R$ '))

            if saque > 0 and saque <= saldo_Inicial:

                saldo_Inicial -= saque
                print(f'Saque realizado com Sucesso!!! R$ {saque:.2f}\n')

            else:
                print('Saque inválido ou saldo Insuficiente\n')

        elif op == '4':
            print('Obrigado por utilizar nosso Caixa')

            break
        else:
            print('Operação inválida. Por Favor tente novamente!\n')
opcao()

