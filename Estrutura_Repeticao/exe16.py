def fibonacci():
    fn = int(input('Informe o ultimo número: '))
    a = 0
    b = 1
    
    while a < fn:
        print(a, end=',')
        a, b = b, a+b

fibonacci()