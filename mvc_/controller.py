import imp

from httplib2 import RETRIES
from dal import PessoaDal
from model import Pessoa

class PessoaController:
    @classmethod
    def Cadastrar(cls,nome,idade,cpf):
        if len(nome) > 2 and  0 < idade < 200 and len(cpf) == 11:
            try:
                PessoaDal.salvar(Pessoa(nome,idade,cpf))
                return True
            except Exception as e:
                return e
        else:
            return False
