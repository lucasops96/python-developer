class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave , valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo
    
    # def __str__(self):
    #     return 'Mamifero'
 
class Ave(Animal):

    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        # print(Ornitorrinco.__mro__)
        Ornitorrinco.mro()
        super().__init__(cor_pelo=cor_pelo,cor_bico=cor_bico, numero_patas=numero_patas)

gato = Gato(numero_patas=4,cor_pelo='branco')
print(gato)

ornitorrinco = Ornitorrinco(cor_pelo='marrom',cor_bico='laranja',numero_patas=4)
print(ornitorrinco)