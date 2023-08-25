class Veiculos:
    def __init__(self,modelo, cor, placa, numero_rodas):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligando_motor(self):
        print(f'{self.modelo} Ligando o motor ...')
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave , valor in self.__dict__.items()])}"
    
class Moto(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):
    def __init__(self,modelo, cor, placa, numero_rodas, carregado):
        super().__init__(modelo,cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self,):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Moto('POP 100','Preta','NHG-4566',2)
moto.ligando_motor() 

carro = Carro('Gol','Preta','BMM-3218',2)
carro.ligando_motor() 

caminhao = Caminhao('Mercedes','Vermelho','ABD-1234',8,True)
caminhao.ligando_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)