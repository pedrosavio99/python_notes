import imp
import utils
from utils import x #isso serve pra n importar o arquivo inteiro, ganho de performance
from utils import x as x_importado #aqui podemos mudar a nome da varivel
from utils import soma_numeros as soma #importando somas
from minhas_funcoes.minhas_funcs_em_outra_pasta import y as y_pasta #vai concatenando com ponto  se quiser voltar uma pasta use ..

print(utils.x)
print(x_importado)

print(soma(5,10))

print(y_pasta)