def mostra(n1, n2):
    soma = 0
    
    for c in range(n1 +1, n2):
        
        soma += c
    
    print(soma, end=' ')

num1 = int(input('Informe o numero inicial: '))
num2 = int(input('Informe o numero final: '))

mostra(num1, num2)