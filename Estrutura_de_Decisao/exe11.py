def salario(s):
    if s <= 280:
        p = '20 %'
        valor_r = s * 0.2
        reajuste  = s +(s * 0.2)

    elif s > 280 and s <= 700:
        p = '15 %'
        valor_r = s * 0.15
        reajuste = s + (s * 0.15)

    elif s > 700 and s <= 1500:
        p = '10%'
        valor_r = s * 0.10
        reajuste = s + (s * 0.10)

    elif s > 1500:
        p = '5%'
        valor_r = s * 0.05
        reajuste = s + (s * 0.05)

    print(f'O salário inicial foi de R$ {s}\n'
          f'O percentual de aumento aplicado: {p}\n'
          f'O valor do aumento: R$ {valor_r}\n'
          f'Novo salário , após o aumento: R$ {reajuste}') 


sal = float(input("Informe seu salário atual: "))

salario(sal)