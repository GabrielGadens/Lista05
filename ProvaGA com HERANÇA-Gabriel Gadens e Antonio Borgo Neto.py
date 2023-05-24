faunaBR = [
    # [Animal	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Capivara',	True,	True,	True,	True,	True,	True],
    ['Gralha azul',	False,	True,	False,	False,	True,	False],
    ['Tamanduá-bandeira',	True,	True,	True,	False,	True,	False],
    ['Onça pintada',	True,	True,	False,	True,	False,	True],
    ['Tatu-bola',	False,	False,	False,	True,	False,	False]
]

floraBR = [
    # [Planta	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Ipê amarelo',	True,	True,	True,	True,	True,	True],
    ['Araucária',	False,	True,	False,	False,	True,	False],
    ['Mandacaru',	False,	False,	True,	True,	False,	False],
    ['Vitória-régia',	True,	False,	False,	False,	False,	True],
    ['Jatobá',	True,	True,	True,	False,	False,	True]

]

# A:
class SerVivo:
    def __init__(self,nome):
        self._nome=nome
        self._nomeCientifico=''
        self._filo=''
        self._classe=''
        self._familia=''
        self._genero=''
        self._especie=''
        self._estadoConservacao=0

class Bioma():
    def __init__(self,nome):
        self.__nome=nome
        self.__fauna=[]
        self.__flora=[]
    
    def getNome(self):
        return self.__nome
    
    def adicionarAnimal(self,Animal):
        self.__fauna.append(Animal)

    def adicionarVegetal(self,Vegetal):
        self.__flora.append(Vegetal)

    def exibirFauna(self):
        for i in range(len(self.__fauna)):
            print(self.__fauna[i].getNome())

    def exibirFlora(self):
        for i in range(len(self.__flora)):
            print(self.__flora[i].getNome())

class Animal(SerVivo):
    def __init__(self,nome):
        super().__init__(nome)
        print('Animal',self._nome,'criado')

    def getNome(self):
        return self._nome

class Vegetal(SerVivo):
    def __init__(self,nome):
        super().__init__(nome)
        print('Vegetal',self._nome,'criado')

    def getNome(self):
        return self._nome

# B:
B1=Bioma('Amazônia')
B2=Bioma('Mata_Atlântica')
B3=Bioma('Cerrado')
B4=Bioma('Caatinga')
B5=Bioma('Pampa')
B6=Bioma('Pantanal')
Biomas = [B1,B2,B3,B4,B5,B6]
A1=Animal('Capivara')
A2=Animal('Gralha azul')
A3=Animal('Tamanduá-bandeira')
A4=Animal('Onça pintada')
A5=Animal('Tatu-bola')
Animais = [A1,A2,A3,A4,A5]
V1=Vegetal('Ipê amarelo')
V2=Vegetal('Araucária')
V3=Vegetal('Mandacaru')
V4=Vegetal('Vitória-régia')
V5=Vegetal('Jatobá')
Vegetais = [V1,V2,V3,V4,V5]

# C:
for i in range(len(faunaBR)):
    for j in range(1,len(faunaBR[i])):#começo da coluna 1, assim ignoro a 0
        if(faunaBR[i][j]==True):
            Biomas[j-1].adicionarAnimal(Animais[i])
            #pego o j-1 pois a colun 0 são apenas os nomes e como fiz na ordem só utilizo das posições

for i in range(len(floraBR)):
    for j in range(1,len(floraBR[i])): #começo da coluna 1, assim ignoro a 0
        if(floraBR[i][j]==True):
            Biomas[j-1].adicionarVegetal(Vegetais[i]) 
            #pego o j-1 pois a colun 0 são apenas os nomes e como fiz na ordem só utilizo das posições


print('\n',B1.getNome())
print('fauna')
B1.exibirFauna()
print('\nflora')
B1.exibirFlora()

print('\n',B2.getNome())
print('fauna')
B2.exibirFauna()
print('\nflora')
B2.exibirFlora()

print('\n',B3.getNome())
print('fauna')
B3.exibirFauna()
print('\nflora')
B3.exibirFlora()

print('\n',B4.getNome())
print('fauna')
B4.exibirFauna()
print('\nflora')
B4.exibirFlora()

print('\n',B5.getNome())
print('fauna')
B5.exibirFauna()
print('\nflora')
B5.exibirFlora()

print('\n',B6.getNome())
print('fauna')
B6.exibirFauna()
print('\nflora')
B6.exibirFlora()

