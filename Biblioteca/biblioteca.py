# Classe para gerenciar
# Atributos: acervo (uma lista de objetos Livro e Revista) e usuarios (uma lista de objetos Usuario).

#Métodos:
# adicionar_material(material)
# remover_material(material)
# emprestar_material(usuario, titulo): Este método deve verificar se o material existe no acervo e se está disponível. 
# Se sim, remove do acervo e adiciona ao historico_emprestimos do usuario.
# devolver_material(usuario, titulo): Faz o processo inverso.
# consultar_acervo(): Exibe todos os materiais disponíveis no acervo, utilizando o método exibir_informacoes() de cada objeto.

from material import Material
from livro import Livro
from revista import Revista
from usuario import Usuario

class Biblioteca:
    def __init__(self, acervo: list, usuarios: list):
        self.__acervo = acervo
        self.__usuarios = usuarios

    # GET

    def getAcervo(self):
        return self.__acervo
    
    def getUsuarios(self):
        return self.__usuarios
    
    # 

    def setAcervo(self, novo_acervo: list):
        self.__acervo = novo_acervo

    def setUsuarios(self, novo_usuarios: list):
        self.__usuarios = novo_usuarios