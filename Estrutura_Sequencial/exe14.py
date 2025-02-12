def preco_pagar(p):

    excesso = p - 50
    multa = excesso * 4

    print(f'O execesso do limite do peso foi de {excesso:.3f}kg e a multa cobrada será de R$ {multa:.2f}')

peso = float(input('Informe o peso do peixe: '))
preco_pagar(peso)