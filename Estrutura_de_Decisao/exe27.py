ma = float(input('Informe a quantidade em kg na compra de maças: '))
mo = float(input('Informe a quantidade em kg na compra de morangos: '))
 
if ma <= 5:
    valorMa = ma * 1.8
else: 
    valorMa = ma * 1.5

if mo <= 5:
    valorMo = mo * 2.5
else:
    valorMo = mo * 2.2


valor = valorMa + valorMo
if (mo + ma) > 8 or valor > 25:
    desc = valor - (valor * 0.1)
else: 
    desc = 0
    
print(f'A quantidade de Morangos foi de R$ {valorMo}\n'
    f'A quantidade de Maças foi de R$ {valorMa} \n'
    f'O valor a ser pago é de R$ {valor} com desconto será de R$ {desc:.2f}')
    


