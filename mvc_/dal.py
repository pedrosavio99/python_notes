from model import Pessoa


class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoa.txt','w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
    @classmethod   
    def ler(cls):
        nome = 'caio'
        idade = 20
        cpf = 54545

        return Pessoa(nome,idade,cpf)


p1 = Pessoa('pedro',20,'18271872')
PessoaDal.salvar(p1)
print(PessoaDal.ler().nome)