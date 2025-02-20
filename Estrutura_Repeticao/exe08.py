def descubra():
    c = 1
    soma = media = 0
    while c <= 5:
        num = int(input(f'Digite o {c}º numero: '))

        c += 1
        
        soma += num
        media = soma / 5
    
    print(f'A soma dos numero é {soma}')
    print(f'A media dos numeros é {media}')
descubra()