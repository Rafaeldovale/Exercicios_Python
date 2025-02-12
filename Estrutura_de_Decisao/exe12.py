'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende 
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é 
descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá 
pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''


def salario(s, sind, fg):

    if s <= 900:
        des_sindicato = s * sind
        des_fgts  = s * fg
        des_inss = s * 0.10
        tot_desc = des_fgts + des_sindicato + des_inss
        sal_liquido = s - tot_desc

    elif s > 900 and s <= 1500:
        des_ir = s * 0.05
        des_fgts = s* fg
        des_sindicato = s* sind
        des_inss = s * 0.10
        tot_desc = des_ir + des_fgts + des_sindicato + des_inss
        sal_liquido = s - tot_desc

    elif s > 1500 and s <= 2500:
        des_ir = s * 0.10
        des_fgts = s* fg
        des_sindicato = s* sind
        des_inss = s * 0.10
        tot_desc = des_ir + des_fgts + des_sindicato + des_inss
        sal_liquido = s - tot_desc
    
    elif s > 2500:
        des_ir = s * 0.20
        des_fgts = s* fg
        des_sindicato = s* sind
        des_inss = s * 0.10
        tot_desc = des_ir + des_fgts + des_sindicato + des_inss 
        sal_liquido = s - tot_desc 


    print(f' Salário Bruto:         : R$ {s:.2f}\n'
          f'(-) IR                  : R$ {des_ir:.2f}\n'  
          f'(-) INSS                : R$ {des_inss:.2f}\n'
          f'FGTS                    : R$ {des_fgts:.2f}\n'
          f'Total de descontos      : R$ {tot_desc:.2f}\n'
          f'Salário Liquido         : R$ {sal_liquido:.2f}')

sal = float(input('Informe seu salário Bruto: R$ '))
sindicato = 0.03
fgts = 0.11
salario(sal, sindicato, fgts)