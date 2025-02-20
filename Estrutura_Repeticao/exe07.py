def maior():
    c = 1
    maior_num = 1
    
    while c <= 5:
        num = int(input(f'Informar o {c}º numero: '))
        c += 1

        if num > maior_num:
            maior_num = num
    print(maior_num)
   
maior()