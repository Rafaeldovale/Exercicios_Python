def media(n1, n2, n3):
    media_final = (n1 + n2 + n3)/3

    if  media_final < 10:
        print(f'"Aprovado", com a respectiva média alcançada {media_final}')
    elif media_final < 7:
        print(f'"Reprovado", com a respectiva média alcançada {media_final}')
    elif media_final == 10:
        print(f'"Aprovado com Distinção"')
    ...

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media(nota1, nota2, nota3)