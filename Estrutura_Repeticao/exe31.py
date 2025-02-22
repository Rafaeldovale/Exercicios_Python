c = produto = 1

soma = 0 
while True:
    if produto != 0:
        produto = float(input(f'Produto {c}: R$ '))
    else:
        break
    
    soma += produto

    c += 1
print(f'Total: R$ {soma:.2f}')
dinheiro = float(input('Dinheiro: R$ '))
print(f'Troco: R$ {dinheiro - soma:.2f}')
