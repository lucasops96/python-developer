class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor

    def buzinar(self): 
        print('Plim plim ...')

    def parar(self):
        print('Parando bicicleta ...')
        print('Bicicleta parada.')

    def correr(self):
        print('Vrummm ...')

    # def __str__(self):
    #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave , valor in self.__dict__.items()])}"


# b1 = Bicicleta('cromada','GTS',2011,700)
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('azul','stark',2022,1200)
print(b2)