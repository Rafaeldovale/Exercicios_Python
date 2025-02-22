c = alunos = totalunos = 0

turmas = int(input('Qual a quantidade de turmas: '))

while c < turmas: 

    if alunos < 40:
        alunos = int(input('Qual a quantidade de alunos: '))
    else:
        print('Quantidade errada!')

    totalunos += alunos
    c += 1

media_aluno = totalunos / turmas
print(f'A quantidade media de alunos é de {media_aluno}') 