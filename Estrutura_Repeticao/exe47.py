def competicão():

    lista = []
    nome = str(input('Informe o nome da competidora: '))
    for c in range(7):
        
        nota = float(input('Nota: '))
        lista.append(nota)

    soma =  sum(lista)
    media = soma / len(lista)

    print(soma)
    print(f'Resultado Final: \n'
          f'Atleta: {nome}\n'
          f'Melhor nota: {max(lista)}\n'
          f'Pior nota: {min(lista)}\n'
          f'Media: {media:.2f}')


competicão()