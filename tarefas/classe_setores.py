import string
from abc import ABC,abstractmethod 

class Estantes(ABC):
    
    def __init__(self,tipo):
        self.setores = []
        self.subsetores = []
        self.containers = []
        self.tipo = tipo
        self.qnt_subsetores = 6 if self.tipo == 1 else 7
        self.qnt_containers = 6 if self.tipo == 1 else 4
        
    def criar_setores(self,qnt_estantes):
        for i in range(qnt_estantes):
            id_setor = 1 if not self.setores else self.setores[-1][0] + 1
            self.setores.append((id_setor,i+1,self.tipo))
    
    
    def criar_subsetores(self):
        for setor in self.setores:
            for i in range(self.qnt_subsetores):
                id_subsetor = 1 if not self.subsetores else self.subsetores[-1][0] + 1
                self.subsetores.append((id_subsetor,i+1,setor[0]))
    
    def criar_containers(self):
        for subsetor in self.subsetores:
            for i in range(self.qnt_containers):
                id_container = 1 if not self.containers else self.containers[-1][0] + 1
                self.containers.append((id_container,subsetor[0],string.ascii_lowercase[i],0))
    
    def mostrar_setores(self):
        print('Setores')
        for i in self.setores:
            print(i)
    
    def mostrar_subsetores(self):
        print('SubSetores')
        for i in self.subsetores:
            print(i)
    
    def mostrar_containers(self):
        print('Containers')
        for i in self.containers:
            print(i)


class Entradas(Estantes):
    def __init__(self, tipo=1):
        super().__init__(tipo)
    

class Saidas(Estantes):
    def __init__(self, tipo=2):
        super().__init__(tipo)
   


entrada = Entradas()
entrada.criar_setores(5)
entrada.criar_subsetores()
entrada.criar_containers()

entrada.mostrar_setores()
entrada.mostrar_subsetores()
entrada.mostrar_containers()

saida = Saidas()
saida.criar_setores(4)
saida.criar_subsetores()
saida.criar_containers()

saida.mostrar_setores()
saida.mostrar_subsetores()
saida.mostrar_containers()