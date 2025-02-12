def loja():

    area = float(input('Informe o tamanho da área a ser pintada: '))
    
    litros = area / 3.0
    latas = int(litros / 18.0)
    if litros % 18 != 0:
        latas += 1

    valor = latas * 80

    print(f'O tamanho da área a ser pintado será de {area}m²\n'
          f'A quantidade de tinta será de {litros:.3f} então vai ser necessário {latas} Latas de tinta\n'
          f'O valor total da compra será de R$ {valor:.2f}')
loja()