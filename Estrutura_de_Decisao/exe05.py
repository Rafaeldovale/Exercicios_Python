def situacao(n1, n2):
    
    media = (n1 + n2)/2

    if media >= 7 and media < 10:
        print(f'O aluno foi "aprovado" com a nota {media}pts')
    elif media < 7:
        print(f'O aluno foi "reprovado" com a nota {media}pts')
    elif media == 10:
        print(f'O aluno foi "aprovado com Distinção" coma anota {media}pts')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

situacao(nota1, nota2)