def triangulo (t1, t2, t3):
    if (t1 + t2 < t3) or (t1 + t2 < t3) or (t2 + t3 < t1):
        print('Nao é um triangulo')
    elif (t1 == t2) and (t1 == t3) :
        print('Equilatero')
    elif (t1 == t2) or (t1 == t3) or (t2 == t3):
        print('Isósceles')
    else:
        print('Escaleno')
    

tri1 = int(input('Informe o valor da primeira reta : '))
tri2 = int(input('Informe o valor da segunda reta: '))
tri3 = int(input('Informe o valor da terceira reta: '))
triangulo(tri1, tri2, tri3)
