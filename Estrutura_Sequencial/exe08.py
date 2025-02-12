def tot_salario(g, h):
    
    cal = g *  h
    print(f'Você ganaha no total R${cal:.2f} por mês.')

ganha = float(input('Quanto você ganha por hora: '))
hora = float(input('Quanto de horas você trabalha no mês: '))
tot_salario(ganha, hora)