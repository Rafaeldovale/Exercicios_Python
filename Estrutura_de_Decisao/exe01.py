def maior(num1, num2):
    
    if num1 < num2:
        print(f'O numero {num1} é menor que {num2}')
    else:
        print(f'O numero {num2} é menor que {num1}')

n1 = int(input('Digite um valor qualque: '))
n2 = int(input('Digite outro valor qualquer: '))

maior(n1, n2)