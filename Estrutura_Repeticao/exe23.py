numero = int(input('Digite um número: '))

primos = []

divisor= 0

for n in range(2, numero + 1):
    for count in primos:
        if (n % count == 0):
            divisor += 1

    if divisor == 0:
        primos.append(n)

    divisor = 0

print(primos)