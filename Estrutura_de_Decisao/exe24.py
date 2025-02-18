def escolha(n1, n2):
    res = input('Informe a operação que queira fazer: \n'
                f'[A]dição\n'
                f'[M]ultiplicação\n'
                f'[D]ivisão\n'
                f'[S]ubtração: ').upper()
    
    if res == 'A':
        resultado = n1 + n2

    elif res == "M":
        resultado = n1 * n2

    elif res == 'D':
        resultado = n1 / n2
    
    elif res == 'S':
        resultado = n1 - n2

    print(resultado)

    if resultado >= 0:
        print('Positivo')
    else:
        print('Negativo')

    if resultado % 2 == 0:
        print('Par')
    else:
        print('Ímpar')

    if resultado == int(resultado):
        print('inteiro')
    else:
        print('decimal')

num1 = float(input('Informe o primeiro valor: '))
num2 = float(input('Informe o segundo valor: '))
escolha(num1, num2)