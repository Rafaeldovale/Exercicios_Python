def formula(a, b, c):
    
    delta = (b ** 2) + (4 * a * c)
    
    while a != 0:
   
        if delta < 0:
            print('A equação não possui raízes reais!')
            print()
        elif delta == 0:
            print(f'A equação possui apenas uma raiz real, {delta}')
        elif delta >= 0:
            print(f'A equação possui duas raizes, +{delta} e -{delta}')
        break
    
n1 = int(input('Informe o valor de a: '))
n2 = int(input('Informe o valor de b: '))
n3 = int(input('Informe o valor de c: '))
formula(n1, n2, n3)