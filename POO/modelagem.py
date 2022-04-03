#poo = modelagem de entidades e suas caracteristicas

#atributos e metodos -------------- caracterisiticas e funcoes que as entidades podem ter ou fazer

#como modelar em python


class Pessoas:
    raca = 'humano' #esse atributo ira ser herdado igualmente para todos os obejtos criados
    def __init__(self,nome,idade,cpf): #o metodo init sempre será chmada primeiro em um novo objeto
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    #criar um metodo de pessoas,precisa instanciar antes de ser chamado
    def logar_sistema(self): #sempre tem que ter o self
        print(f'{self.nome} esta usando seu metodo de logar no sistema ')


    #criando metodos de classe, esses podem ser acessados sem precisar atribuir nada antes
    @classmethod
    def andar(cls, velocidade):  #perceba que não é mais self, pois o self aponta para a instancia e o cls aponta para a classe inteira
        print(f'estou andando na velocidade de {velocidade} m/s')
        #em metodos de classe podemos criar também atributos de toda a classe mas que so é criando caso seja chamado
        cls.pernas = 2

    #criando metodos utilitarios que n tem acesso a classe
    @staticmethod
    def is_adulto(idade):
        if idade > 18:
            return True
        return False

#como criar uma npva pessoa/objeto

p1 = Pessoas('tibis',20,'4545454554')

#como acessar os atributos de um objeto
print(p1)
print(p1.nome, p1.cpf)
print(Pessoas.raca) #atributo para todos os objetos criados

#sobre esses atributos globais de class observe que podem ser mudados de apenas um objeto 
#ou de toda a classe
p1.raca = 'diferente dos iguais'
print(p1.raca)
print(Pessoas.raca)

#chamar um metodo de pessoas

p1.logar_sistema()

#acessando metodos de toda a classe

p1.andar(5) #as instancias podem acessar tbm
Pessoas.andar(7) #mas apenas as classes também podem acessar pois é um metodo global

#chamando o atributo de pernas do cls

print(Pessoas.pernas)


#chamando metodo statico utilitario

print(Pessoas.is_adulto(20))
