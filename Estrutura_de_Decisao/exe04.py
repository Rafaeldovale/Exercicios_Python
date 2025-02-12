def definir(l):

    if l in 'aeiou':
        print('Você digitou uma vogal')
    else:
        print('Você digitou uma consoante')

letras = str(input('Digite uma letra: ')).lower()
definir(letras)