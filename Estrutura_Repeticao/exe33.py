def temperatura(*args):

    media =  sum(args) / len(args)
    return media

temp = list(map(float,input('Digite o conjunto de temperaturas anotadas: ').split()))
media = temperatura(*temp)
print(f'A media foi: {media}')
print(f'O valor maximo foi: {max(temp)}')
print(f'O valor minino foi: {min(temp)}')