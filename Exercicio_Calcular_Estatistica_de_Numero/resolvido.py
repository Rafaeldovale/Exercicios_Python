def estatistica(*args):

    media = sum(args) / len(args)
    return media


total = list(map(float, input('Digite uma sequeência de número: ').split()))
m_total = estatistica(*total)
print(f'A media da soma dos núemros é: {m_total}')
print(f'O maior valor é {max(total)}')
print(f'O menor valor é {min(total)}')