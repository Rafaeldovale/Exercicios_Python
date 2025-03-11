def menu():

    
    op = input('Informe qual conversão quer fazer: \n'
               '[A] - Celsius para Farenheit\n'
               '[B] - Farenheit para Celsius ').upper().split()
    
    if op == "A":
        
        celsius_farenheit()
    
    if op == "B":

        farenheit_celsius()
    
    
def farenheit_celsius():
    
    valor = int(input('Informe o valor a ser convertido para Farenheit: '))

    c = (valor - 32) * (5 /9)

    print(f'O resultado é {c}')

    

def celsius_farenheit():

    valor = int(input('Informe o valor a ser convertido para Celsius: '))

    f = (valor * (9 /5)) + 32

    print(f'O resultado é {f}')

menu()
celsius_farenheit()
