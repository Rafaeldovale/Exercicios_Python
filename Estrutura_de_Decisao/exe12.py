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