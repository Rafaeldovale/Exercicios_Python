def salario():

    hora = float(input('Qual o valor da sua hora trabalhada: R$ '))
    totSalario  = hora * 220

    inss = totSalario * 0.08
    ir = totSalario * 0.11
    sindicato = totSalario * 0.05
    salarioLiquido = totSalario - inss - ir - sindicato

    print(f'+ Salário Bruto : R$ {totSalario:.2f}\n'
          f'- IR (11%) : R$ {ir:.2f}\n'
          f'- INSS (8%) : R$ {inss:.2f}\n'
          f'- Sindicato (5%) : R$ {sindicato:.2f}\n'
          f'= Salário Liquido : R$ {salarioLiquido:.2f}')

salario()