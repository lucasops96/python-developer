from abc import ABC, abstractmethod, abstractproperty


class Controle(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(Controle):
    def ligar(self):
        return print('ligando a tv ..., tv ligada')
    
    def desligar(self):
        return print('desligando a tv ..., tv desligada')
    
    @property
    def marca(self):
        return print('LG')


c = ControleTV()
c.ligar()
c.marca
c.desligar()