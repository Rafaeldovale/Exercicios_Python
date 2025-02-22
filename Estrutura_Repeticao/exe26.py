def eleitores(qnt):
    c = 0
    cam1 = cam2 = cam3 = 0
    while c < qnt:

        candidato = (input('Em qual candidato ira votar: [P]rimeiro, [S]egundo, [T]erceiro: ')).upper()
        

        if candidato == 'P':
            cam1 += 1

        elif candidato == 'S':
            cam2 += 1
        
        elif candidato == 'T':
            cam3 += 1

        c += 1
        
    print(f'O primeiro candidato teve {cam1} votos\n'
          f'O segundo candidato teve {cam2} votos\n'
          f'O terceiro candidato teve {cam3} votos\n')


quantidade = int(input('Quantos eleitores irão votar: '))
eleitores(quantidade)