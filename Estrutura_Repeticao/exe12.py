def tabuada(n):

    for c in range(1, 11):
        print(f'{c} X {n} = {c * n}')

num = int(input('Qual tabuada deseja ver: '))
tabuada(num)