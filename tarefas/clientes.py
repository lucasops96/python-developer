from abc import ABC, abstractmethod
import os

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
    
    def pesquisa_tipo_cliente(self, tipo_cliente):
        print(f'Clientes do tipo {tipo_cliente}')
        for cliente in self.lista_clientes:
            if cliente['tipo_cliente'] == tipo_cliente:
                print(cliente,'\n')
    
    def pesquisa_documento(self,tipo_cliente, documento):
        for cliente in self.lista_clientes:
            if cliente['tipo_cliente'] == tipo_cliente and cliente['cpf' if tipo_cliente == 'Física' else 'cnpj'] == documento:
                return print(cliente)

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


# p1 = Fisica('Padre Miguel','88','centro','6225000','Patolândia','Paraíba','Física','05655892375','Miguel')
# p1.cadastrar_cliente()


# p6 = Juridica('Padre Miguel','88','centro','6225000','Patolândia','Paraíba','Jurídica','12.345.678/0003-00','Luqueta Store')
# p6.cadastrar_cliente()

# p1.pesquisa('Jurídica','12.345.678/0003-00')
# p1.pesquisa('Física','05655892375')


op = 1

while op != 0:
    op = int(input('1-PARA CADASTRAR CLIENTE FISÍCO\n2-PARA CADASTRAR CLIENTE JURÍDICO\n3-PESQUISAR POR TIPO CLIENTE\n4-PESQUISAR POR DOCUMENTO\n: '))

    if op == 1:
        cpf = input('Digite o CPF: ')
        nome = input('Digite o Nome: ')
        rua = ''
        numero = ''
        bairro = ''
        cep = ''
        cidade = input('Digite a Cidade: ')
        estado = input('Digite o Estado: ')
        tipo_cliente = 'Física'

        if not cpf.isnumeric():
            os.system('clear')
            print('CPF inválido, digite apenas números.')
            
        
        elif len(cpf) != 11:
            os.system('clear')
            print('CPF inválido, quantidade de digitos deve ser 11.')
    
        else:
            cpf = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
            pf = Fisica(rua,numero,bairro,cep,cidade,estado,tipo_cliente,cpf,nome)
            pf.cadastrar_cliente()
            os.system('clear')
            print('CLIENTE CADASTRADO\n')
    
    elif op == 2:
        cnpj = input('Digite o CNPJ: ')    
        razao_social = input('Digite a Razão Social: ')
        rua = ''
        numero = ''
        bairro = ''
        cep = ''
        cidade = input('Digite a Cidade: ')
        estado = input('Digite o Estado: ')
        tipo_cliente = 'Jurídica'

        if not cnpj.isnumeric():
             os.system('clear')
             print('CNPJ inválido, digite apenas números.')
        
        elif len(cnpj) != 14:
            os.system('clear')
            print('CNPJ inválido, quantidade de digitos deve ser 14.')
            
        
        else:
            cnpj = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
            pj = Juridica(rua,numero,bairro,cep,cidade,estado,tipo_cliente,cnpj,razao_social)
            pj.cadastrar_cliente()
            os.system('clear')
            print('CLIENTE CADASTRADO\n')
            
    
    elif op == 3:
        os.system('clear')
        tipo = int(input('1-PARA PESQUISAR CLIENTES FÍSICO\n2-PARA CLIENTES JURÍDICOS\n:'))
        pf.pesquisa_tipo_cliente('Física' if tipo == 1 else 'Jurídica')
        
    
    elif op == 4:
        os.system('clear')
        doc = input('Digite CPF/CNPJ: ')
        if doc.isnumeric():
            if len(doc) == 11:
                os.system('clear')
                tipo_cliente_doc = 'Física'
                doc = f'{doc[0:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:11]}'
                pf.pesquisa_documento(tipo_cliente_doc,doc)
            
            elif len(doc) == 14:
                os.system('clear')
                tipo_cliente_doc = 'Jurídica'
                doc = f'{doc[0:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:14]}'
                pf.pesquisa_documento(tipo_cliente_doc,doc)
            
            else:
                os.system('clear')
                print('Erro de digitação ou valores não encontrados.')
    
        else:
            os.system('clear')
            print('Documento inválido, digite apenas números.')
            


