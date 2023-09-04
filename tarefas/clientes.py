from abc import ABC, abstractmethod

class Clientes(ABC):
    lista_clientes = []

    def __init__(self,rua, numero, bairro, cep, cidade, estado,tipo_cliente):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.tipo_cliente = tipo_cliente
    
    @abstractmethod
    def cadastrar_cliente(self):
        pass

    def imprimir_clientes(self):
        for i in self.lista_clientes:
            print(i,'\n')
    
    def pesquisa(self,tipo_cliente, chave):
        for i in self.lista_clientes:
            if i['tipo_cliente'] == tipo_cliente and i['cpf' if tipo_cliente == 'Física' else 'cnpj'] == chave:
                return print(i)


class Fisica(Clientes):
    def __init__(self,rua, numero, bairro, cep, cidade, estado, tipo_cliente,cpf,nome):
        super().__init__(rua, numero, bairro, cep, cidade, estado, tipo_cliente)
        self.cpf = cpf
        self.nome = nome

    def cadastrar_cliente(self,):
        self.lista_clientes.append({
            'cpf':f'{self.cpf}',
            'nome':f'{self.nome}',
            'rua':f'{self.rua}',
            'numero':f'{self.numero}',
            'bairro':f'{self.bairro}',
            'cep':f'{self.cep}',
            'cidade':f'{self.cidade}',
            'estado':f'{self.estado}',
            'tipo_cliente':f'{self.tipo_cliente}',
        })


class Juridica(Clientes):
    def __init__(self, rua, numero, bairro, cep, cidade, estado, tipo_cliente,cnpj, razao_social):
        super().__init__(rua, numero, bairro, cep, cidade, estado, tipo_cliente)
        self.cnpj = cnpj
        self.razao_social = razao_social

    def cadastrar_cliente(self):
        self.lista_clientes.append({
            'cnpj':f'{self.cnpj}',
            'razao_social':f'{self.razao_social}',
            'rua':f'{self.rua}',
            'numero':f'{self.numero}',
            'bairro':f'{self.bairro}',
            'cep':f'{self.cep}',
            'cidade':f'{self.cidade}',
            'estado':f'{self.estado}',
            'tipo_cliente':f'{self.tipo_cliente}',
        })

p1 = Fisica('Padre Miguel','88','centro','6225000','Patolândia','Paraíba','Física','05655892375','Miguel',)
p1.cadastrar_cliente()

p2 = Juridica('Padre Miguel','88','centro','6225000','Patolândia','Paraíba','Jurídica','12.345.678/0003-00','Luqueta Store')
p2.cadastrar_cliente()

# p1.pesquisa('Jurídica','12.345.678/0003-00')
p1.pesquisa('Física','05655892375')