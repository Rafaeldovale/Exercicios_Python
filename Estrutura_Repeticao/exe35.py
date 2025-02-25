def tabuada(t, n1, n2):

    print(f'Vou montar a tabuada de {t} começando em {n1} e terminando em {n2}')
    for c in range(n1, n2 + 1):
        if n1 < n2:
            print(f'{t} x {c} = {t * c}')
        else: 
            print('Você deve informar o valor inicial menor que o final')

tab = int(input('Qual tabuada será analisada: '))
num1 = int(input('Informe qual numero vai iniciar: '))
num2 = int(input('Informe qual numero vai terminar: '))
tabuada(tab, num1, num2)