
class Pessoa:  #essa classe ira ser herdada por cliente e vendedor, por isso podem acessar seus atributos e metodos
    
    def andar(self):
        print('estou vendendo')

class Cliente(Pessoa):  #forma de herdar atributos de outra classe é passando ela nos parentes
    def comprar(self):
        print('Estou comprando')

class Vendedor(Pessoa):
    def vender(self):
        print('estou vendendo')


v1 = Vendedor()
v1.andar()

#porem ele n pode acessar o atributo comprar que so cliente tem, mas cliente tbm pode andar pois tbm é uma pessoas