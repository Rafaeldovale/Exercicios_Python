def maior(n1, n2, n3):

    if n1 >= n2 and n1 >= n3:
        print(f'O valor {n1}')
    elif n2 >= n1 and n2 >= n3:
        print(f'O valor {n2}')
    elif n3 >= n1 and n3 >= n2:
        print(f'O valor {n3}')
    
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior(num1, num2, num3)