totVotos = int(input('Quantas pessoas votam nessa secão: '))
totCandidato = totNulo = totBranco = 0
can1 = can2 = can3 = can4 = 0
c = 1
while c <= totVotos:
    opção = input('Escolha a opção desejada: \n'
                '[1] - João \n'
                '[2] - José \n'
                '[3] - Maria \n'
                '[4] - Tardeu \n'
                '[5] - Voto Nulo \n'
                '[6] - Voto Branco ')
    c += 1

    if opção == '1':
        can1 += 1

    elif opção == '2':
        can2 += 1

    elif opção == '3':
        can3 += 1

    elif opção == '4':
        can4 += 1

    elif opção == '5':
        totNulo += 1

    elif opção == '6':
        totBranco += 1

print(f'O candidato João teve {can1} votos')
print(f'O candidato Jose teve {can2} votos')
print(f'A candidata Maria teve {can3} votos')
print(f'O candidato Tadeu teve {can4} votos')

print(f'A quantidade de votos brancos foi de {totBranco}')
print(f'A quantidade de votos nulos foi de {totNulo}')

print(f'O percentual de votos brancos foi de {(totBranco/totVotos) * 100}%')
print(f'O percentual de votos nulos foi de {(totNulo/totVotos) * 100}%')