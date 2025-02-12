def mostrar(n1, n2, n3):

    if n1 >= n2 >= n3:
        print(f'O valor {n1} é maior e {n3} é o menor valor')
    elif n2 >= n3 >= n1:
        print(f'O valor {n2} é maior e {n1} é o menor valor')
    elif n3 >= n2  >= n1:
        print(f'O valor {n3} é maior e {n1} é o menor valor')
    elif n3 >= n1 >= n2:
        print(f'O valor {n3} é maior e {n2} é o menor valor')
    elif  n1 >= n3 >= n2:
        print(f'O valor {n1} é maior e {n2} é o menor valor')
    elif n2 >= n1 >= n3:
        print(f'O valor {n2} é maior e {n3} é o menor valor')

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

mostrar(num1, num2, num3)