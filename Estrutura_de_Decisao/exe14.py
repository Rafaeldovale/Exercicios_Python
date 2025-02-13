def media (n1, n2):

    m = (n1 + n2)/2

    if m >= 9 and m <= 10:
        print(f'Sua notas são: {n1} e {n2} \n' 
              f'Sua media foi {m} e o conceito é A\n '
              '"Aprovado"')
    
    elif m >= 7.5 and m < 9:
        print(f'Sua notas são: {n1} e {n2} \n' 
              f'Sua media foi {m} e o conceito é B\n '
              '"Aprovado"')
    
    elif m >= 6 and m <7.5:
        print(f'Sua notas são: {n1} e {n2} \n' 
              f'Sua media foi {m} e o conceito é C\n '
              '"Aprovado"')

    elif m >= 4 and m < 6:
       print(f'Sua notas são: {n1} e {n2} \n' 
              f'Sua media foi {m} e o conceito é D\n '
              '"Reprovado"')
        
    elif m >= 0 and m < 4:
        print(f'Sua notas são: {n1} e {n2} \n' 
              f'Sua media foi {m} e o conceito é E\n '
              '"Reprovado"')
        
num1 = float(input('Entre com sua primeira nota: '))
num2 = float(input('Digite o segundo numero: '))

media(num1,num2)