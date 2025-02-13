while True:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    escolha = input('Qual opção vai escolher: \n'
                    '[A]dição [S]ubtração [M]ultiplicação [d]ivisão sa[i]r: ').upper()
    
    if escolha == 'A':
        soma = n1 + n2
        print(f'Soma = {soma}')
        
    elif escolha == 'S':
        sub = n1 - n2
        print(f'Subtração = {sub}')
        
    elif escolha  == 'M':
        mult = n1 * n2
        print(f'Multiplicação = {mult}')

    elif escolha == 'D':
        div =  n1 / n2
        print(f'Divisão = {div}')

    elif escolha == 'I':
        break

