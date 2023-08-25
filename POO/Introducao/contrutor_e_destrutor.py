class Cachorro:
    def __init__(self,nome,cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo cachorro ...')
    
    def falar(self):
        return print('au au au ...')


c = Cachorro('Bob', 'amarelo')
print(c.nome)
c.falar()
