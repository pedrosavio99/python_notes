
class Pessoa:  #essa classe ira ser herdada por cliente e vendedor, por isso podem acessar seus atributos e metodos   
    def andar(self):
        print('estou andando')

class Vendedor(Pessoa):  #aqui vai rolar a sobreposicao de metodos com o metodo super que sempre aponta para a classe pai
    def vender(self):
        print('estou vendendo')

    def andar(self):
        super().andar() #com o super ele ira chamar primeiro o metodo pai e so depois vai executar o que vem adiante
        print('estou correndo') #sem o super isso iria sobrescrever o metodos pai e nem iria pirnta o andando


v1 = Vendedor()
v1.andar()

#porem ele n pode acessar o atributo comprar que so cliente tem, mas cliente tbm pode andar pois tbm é uma pessoas


#COMO CHAMAR ATRIBUTOS AO INVES DE METODOS

class Pessoa2:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa2):
    def __init__(self, idcliente, nome, idade):
        super().__init__(nome, idade)
        self.id = idcliente  #perceba que eu so precisei atribuir a varivel id pois as outras foram herdadas de Pessoa


c1 = Cliente(5,'pedro',15)

print(c1.nome, c1.idade, c1.id)