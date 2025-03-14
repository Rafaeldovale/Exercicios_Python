print('Gabarito da Prova:\n 01 - A\n 02 - B\n 03 - C\n 04 - D\n 05 - E\n 06 - E\n 07 - D\n 08 - C\n 09 - B\n 10 - A')
gabarito = ''
gabarito2 = ''
count = tot_acertos = tot = count2 = maior = menor = 0


print("-="*30)
continuar = ' '
while continuar != 'N':

    tot_acertos = 0

    for c in range(1,11):
        resposta = input(f"{c} - Resposta da questao: ").strip().upper()[0]
        if c == 1:
            if resposta == 'A':
                count += 1
                tot_acertos += 1
        if c == 2:
            if resposta == 'B':
                count += 1
                tot_acertos += 1
        if c == 3:
            if resposta == 'C':
                count += 1
                tot_acertos += 1
        if c == 4:
            if resposta == 'D':
                count += 1
                tot_acertos += 1
        if c == 5:
            if resposta == 'E':
                count += 1
                tot_acertos += 1
        if c == 6:
            if resposta == 'E':
                count += 1
                tot_acertos += 1
        if c == 7:
            if resposta == 'D':
                count += 1
                tot_acertos += 1
        if c == 8:
            if resposta == 'C':
                count += 1
                tot_acertos += 1
        if c == 9:
            if resposta == 'B':
                count += 1
                tot_acertos += 1
        if c == 10:
            if resposta == 'A':
                count += 1
                tot_acertos += 1
            print("-="*30)
            continuar = input("Quer continuar [S]im [N]ão ").upper()
            tot+=1

        if tot_acertos > maior:
            maior = tot_acertos
        if tot_acertos < menor or tot_acertos == 1:
            menor = tot_acertos

print("-="*30)

print(f"Total de acertos: {count}")
print(f"Pontos recebidos: {count}")
print(f"Maior acerto {maior}")
print(f"Menor acerto: {menor}")
print(f"Total de alunos a utilizar o sistema: {tot}")