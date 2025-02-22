def separador():
    par = impar = 0
    c = 1
    
    while c < 10:
        num = int(input(f'Informe o {c}º número: '))
        
        if num % 2 == 0:
            par += 1

        else:
            impar += 1  
        
        c += 1
    print(f'O total de pares foram {par} e os ímpares foram {impar}')


separador()