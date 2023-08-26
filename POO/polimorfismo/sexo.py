class Sexo:
    def tipo(self):
        print('Tipo de sexo')

class Homem(Sexo):
    def tipo(self):
        print('Masculino')

class Mulher(Sexo):
    def tipo(self):
        print('Feminino')

def mostar_sexo(obj):
    obj.tipo()


mostar_sexo(Homem())
mostar_sexo(Mulher())