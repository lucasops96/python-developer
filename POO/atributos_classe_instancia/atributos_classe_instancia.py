class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"


e1 = Estudante('Guilherme', 45236)
e2 = Estudante('Maria', 65451)

print(e1)
print(e2)