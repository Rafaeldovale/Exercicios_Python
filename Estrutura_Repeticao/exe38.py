alunos = []

# Leitura dos dados dos alunos
for i in range(3):
  numero_aluno = int(input(f"Digite o número do aluno {i + 1}: "))
  altura = int(input(f"Digite a altura do aluno {i + 1} em centímetros: "))
  alunos.append((numero_aluno, altura))

# Encontrando o aluno mais alto e o mais baixo
aluno_mais_alto = alunos[0]
aluno_mais_baixo = alunos[0]

for aluno in alunos:
  if aluno[1] > aluno_mais_alto[1]:
    aluno_mais_alto = aluno
  if aluno[1] < aluno_mais_baixo[1]:
    aluno_mais_baixo = aluno

# Imprimindo os resultados
print("\nAluno mais alto:")
print(f"Número: {aluno_mais_alto[0]}")
print(f"Altura: {aluno_mais_alto[1]} cm")

print("\nAluno mais baixo:")
print(f"Número: {aluno_mais_baixo[0]}")
print(f"Altura: {aluno_mais_baixo[1]} cm")