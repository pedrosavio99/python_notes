#utilizando multiplas herancas 
class Animal:
    def andar(self):
        print('estou andando')
    def morder(self):
        print('estou mordendo')

a1 = Animal()
a1.andar()

class Felino(Animal):  #aqui so estou herdando apenas animal
    def arranhar(self):
        print('estou arranhando')

class Gato(Felino):  #aqui vou herdar felino e animal
    def miar(self):
        print('estou miando')

g1 = Gato()
g1.andar() #herdou de animal
g1.arranhar() #herdou de felino
g1.miar() #classe propria