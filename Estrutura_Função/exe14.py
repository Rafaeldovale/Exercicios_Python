def adicionar(n1, n2):
    
    return n1 + n2

def subtrair(n1, n2):
    
    return n1 - n2

def multiplicar(n1, n2):
    
    return n1 * n2

def dividir(n1, n2):
    
    return n1 / n2


num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

op = input("Escolha a operação desejada: [adicionar], [subtrair], [multiplicar], [dividir] ").lower()

if op == "adicionar":

    resultado = adicionar(num1, num2)

elif op == "subtrair":

    resultado = subtrair(num1, num2)

elif op == "multiplicar":

    resultado = multiplicar(num1, num2)

elif op == "dividir":

    resultado = dividir(num1, num2)

else: 
    
    print('Operação Inválida!')
    
print(f'O resultado foi {resultado}')