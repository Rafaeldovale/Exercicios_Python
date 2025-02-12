def media(a, b, c, d):
    med = (a +b + c + d)/4
    return med

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

resul = media(n1, n2, n3, n4)
print(resul)