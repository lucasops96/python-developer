from datetime import datetime


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
    @classmethod
    def criar_pessoa_data(cls,nome, dia, mes, ano):
        ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
        idade = ano_atual - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return 'É maior de idade' if idade >= 18 else 'Não é maior de idade'


p1 = Pessoa.criar_pessoa_data('Miguel',19,4,2002)
print(f'{p1.nome} tem {p1.idade}')
print(p1.maior_idade(21))