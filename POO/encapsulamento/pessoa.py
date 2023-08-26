from datetime import datetime


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
        return ano_atual - self.ano_nascimento
    

p1 = Pessoa('João', 1995)
print(f'{p1.nome} tem {p1.idade} anos.')
