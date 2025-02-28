def crescimento(a, b):
    ano = 0

    while a <= b:
        a += a * 0.03
        b += b * 0.015
        ano += 1

    print ( "A ultrapassa ou iguala a B em %d anos" %ano )

populaçãoA = int(input('Informe a quantidade da população A: '))
populaçãoB = int(input('Informe a quantidade da população B: '))
crescimento(populaçãoA, populaçãoB)