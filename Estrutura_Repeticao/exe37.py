pesoValor = []
alturaValor =  []
peso = altura = 1
c = 0
while True:
    codigo = int(input('Informe o código de registro: '))
    if codigo != 0:
        
        
        peso = int(input('Qual o peso: '))
        pesoValor.append(peso)
        
        altura = int(input('Qual a alutra: '))
        alturaValor.append(altura)

        c += 1
    else:
        break

print(f'O maior peso = {max(pesoValor)} kg')
print(f'O menor peso = {min(pesoValor)} kg')
print(f'O maior altura = {max(alturaValor)} m')
print(f'O menor altura = {min(alturaValor)} m')
