'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o 
programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    º salários até R$ 280,00 (incluindo) : aumento de 20%
    º salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    º salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    º salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    º o salário antes do reajuste;
    º o percentual de aumento aplicado;
    º o valor do aumento;
    º o novo salário, após o aumento.'''

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