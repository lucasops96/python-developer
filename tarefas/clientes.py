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
    
    
    def pesquisa_tipo_cliente(self, tipo_cliente):
        os.system('clear')
        print(f'Clientes do tipo {tipo_cliente}')
        for cliente in self.lista_clientes:
            if cliente['tipo_cliente'] == tipo_cliente:
                print(cliente,'\n')
    
    def pesquisa_documento(self,documento):
        os.system('clear')
        if not documento.isnumeric():
            return print('Documento inválido, digite apenas números')
        else:
            if len(doc) == 11:
                tipo_cliente = 'Física'
                documento = formatar_cpf(documento)
            elif len(doc) == 14:
                tipo_cliente = 'Jurídica'
                documento = formatar_cnpj(documento)

            for cliente in self.lista_clientes:
                if cliente['tipo_cliente'] == tipo_cliente and cliente['cpf' if tipo_cliente == 'Física' else 'cnpj'] == documento:
                    return print(f'Cliente do documento {documento}: {tipo_cliente}\n',cliente,'\n')
        
        return print(f'Nenhum cliente cadastrado com esse documento: {documento}\n')
    
    
    

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


def formatar_cpf(cpf):
    cpf = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
    return cpf

def formatar_cnpj(cnpj):
    cnpj = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return cnpj

def validar_cpf(cpf):
    os.system('clear')
    if not cpf.isnumeric():
        print('CPF inválido, digite apenas números.')
        return False
    
    elif len(cpf) != 11:
        print('CPF inválido, quantidade de digitos deve ser 11.')
        return False
    
    cpf = formatar_cpf(cpf)
    return cpf 
    
def validar_cnpj(cnpj):
    os.system('clear')
    if not cnpj.isnumeric():
        print('CNPJ inválido, digite apenas números.')
        return False
    
    elif len(cnpj) != 14:
        print('CNPJ inválido, quantidade de digitos deve ser 14.')
        return False
    
    cnpj = formatar_cnpj(cnpj)
    return cnpj



# p1 = Fisica('Padre Miguel','88','centro','6225000','Patolândia','Paraíba','Física','05655892375','Miguel')
# p1.cadastrar_cliente()


# p6 = Juridica('Padre Miguel','88','centro','6225000','Patolândia','Paraíba','Jurídica','12.345.678/0003-00','Luqueta Store')
# p6.cadastrar_cliente()

# p1.pesquisa('Jurídica','12.345.678/0003-00')
# p1.pesquisa('Física','05655892375')


op = 1

while op != 0:
    
    op = int(input('1-PARA CADASTRAR CLIENTE FISÍCO\n2-PARA CADASTRAR CLIENTE JURÍDICO\n3-PESQUISAR POR TIPO CLIENTE\n4-PESQUISAR POR DOCUMENTO\n0-PARA SAIR DO SISTEMA\n: '))
    # cadastro pesso f[isdica]
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

        cpf = validar_cpf(cpf)

        if cpf:
            pf = Fisica(rua,numero,bairro,cep,cidade,estado,tipo_cliente,cpf,nome)
            pf.cadastrar_cliente()
            print('CLIENTE CADASTRADO\n')
        
    # cadastro pessoa juridica
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

        cnpj = validar_cnpj(cnpj)

        if cnpj:
            pj = Juridica(rua,numero,bairro,cep,cidade,estado,tipo_cliente,cnpj,razao_social)
            pj.cadastrar_cliente()
            print('CLIENTE CADASTRADO\n')
            
    # pesquisar clientes físicos ou jurídicos
    elif op == 3:
        tipo = int(input('1-PARA PESQUISAR CLIENTES FÍSICO\n2-PARA CLIENTES JURÍDICOS\n:'))
        if tipo == 1 or tipo == 2:
            pf.pesquisa_tipo_cliente('Física' if tipo == 1 else 'Jurídica')
        else:
            print('Digito errado, tente novamente.')
        
    # pesquisar um cliente pelo documento
    elif op == 4:
        doc = input('Digite CPF/CNPJ: ')
        pf.pesquisa_documento(doc)
    
       


