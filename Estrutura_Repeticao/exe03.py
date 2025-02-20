'''Faça um programa que leia e valide as seguintes informações:
        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd';'''

while True:
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    salario = float(input('Informe seu salario: '))
    sexo = str(input('Qual o seu sexo: [M/F]')).upper()
    estado_civil = str(input('Qual o seu estado civil [s]olteiro, [c]asado, [v]iúvo, [d]ivorciado: ')).upper()

    if len(nome) >3: 
        print(nome)
    else:
        print('Numero de caractere menor que o permitido')

    if 0 < idade <= 100:
        print(idade)
    else:
        print('Idade fora da faixa permitida!')

    if salario > 0:
        print(salario)
    else:
        print('Salário não pode ser igual a zero!')

    if sexo == 'M':
        print('Sexo Masculino!')
    elif sexo == 'F':
        print('Sexo feminino')
    else:
        print('Sexo inválido')

    if estado_civil == 'C':
        print('Casado')
    elif estado_civil == 'S':
        print('Solteiro')
    elif estado_civil == 'V':
        print('Viúvo')
    elif estado_civil == 'D':
        print('Divorciado')
    else:
        print('Valor indefinido')