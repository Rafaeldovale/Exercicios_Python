def tempo(t, v):
    
    print('Tempo aproximado de download: %.0f Minutos ' %((t / v) * 60))

tam = float(input('Tamanho do arquivo (MB): '))
vel = float(input('Velocidade de Internet (MBps): '))
tempo(tam, vel)