import string

def criar_setores(setores,qnt_estantes, tipo):
    for i in range(qnt_estantes):
        id_setor = 1 if not setores else setores[-1][0] + 1
        setores.append((id_setor,i+1,tipo))
        

def criar_subsetores(subsetores,setores):
    for setor in setores:
        if setor[2] == 1:
            for i in range(6):
                id_subsetor = 1 if not subsetores else subsetores[-1][0] + 1
                subsetores.append((id_subsetor,i+1,setor))
        if setor[2] == 2:
            for i in range(7):
                id_subsetor = 1 if not subsetores else subsetores[-1][0] + 1
                subsetores.append((id_subsetor,i+1,setor))


def criar_containers(containers, subsetores):
    for subsetor in subsetores:
        if subsetor[2][2] == 1:
            for i in range(6):
                id_container = 1 if not containers else containers[-1][0] + 1
                containers.append((id_container,subsetor,string.ascii_lowercase[i],0))
        if subsetor[2][2] == 2:
            for i in range(4):
                id_container = 1 if not containers else containers[-1][0] + 1
                containers.append((id_container,subsetor,string.ascii_lowercase[i],0))
    

tipo_setor = [(1,'entrada'),(2,'saida')]
setores = []
subsetores = []
containers = []

criar_setores(setores,5,1)
criar_setores(setores,4,2)
criar_subsetores(subsetores,setores)
criar_containers(containers,subsetores)

print('Setores')
for i in setores:
    print(i)
print('Subsetores')
for i in subsetores:
    print(i)

print('Containers')
for i in containers:
    print(i)