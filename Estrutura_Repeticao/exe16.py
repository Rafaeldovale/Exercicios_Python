'''A valor seja maior que 500.'''
série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o 
def fibonacci():
    fn = int(input('Informe o ultimo número: '))
    a = 0
    b = 1
    
    while a < fn:
        print(a, end=',')
        a, b = b, a+b

fibonacci()