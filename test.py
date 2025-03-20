class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def frear(self):

        self.velocidade -= 10
        
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Velocidade atual: {self.velocidade} Km/h")

    def acelerar(self):

        self.velocidade += 10

        print(f"Velocidade atual: {self.velocidade} Km/h")

    def exibir_info(self):

        print(f'Marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}')

lista_carros = []

while True:

    print('\n-----Menu-----')
    print('1. Adicionar novo carro')
    print('2. Exibir informações do carros')
    print('3. Acelerar um carro')
    print('4. Frear um carro')
    print('5. sair')


    escolha = input('Escolha uma opção: ')

    if escolha == '1':

        marca = input('Digite a marca do carro: ')
        modelo = input('Digite o modelo do carro: ')
        cor = input('Digite a cor')

        novo_carro = Carro(marca, modelo, cor)
        lista_carros.append(novo_carro)

    if escolha == '2':

        if lista_carros:
            for carro in lista_carros:
                carro.exibir_info()

        else:
            print('Nenhum carro add ainda.')


    if escolha == 3:
        ...

    if escolha == 4:
        ...

    if escolha == 5:
        print('Saindo do programa')
        break