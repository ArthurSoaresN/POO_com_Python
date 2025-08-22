# Classe para gerenciar
# Atributos: acervo (uma lista de objetos Livro e Revista) e usuarios (uma lista de objetos Usuario).

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
    
    # SET

    def setAcervo(self, novo_acervo: list):
        self.__acervo = novo_acervo

    def setUsuarios(self, novo_usuarios: list):
        self.__usuarios = novo_usuarios

#Métodos:
# adicionar_material(material)
# remover_material(material)
# emprestar_material(usuario, titulo): Este método deve verificar se o material existe no acervo e se está disponível. 
# Se sim, remove do acervo e adiciona ao historico_emprestimos do usuario.
# devolver_material(usuario, titulo): Faz o processo inverso.
# consultar_acervo(): Exibe todos os materiais disponíveis no acervo, utilizando o método exibir_informacoes() de cada objeto.

    def AdicionarMaterial(self, Item):
        if isinstance(Item, Material):
            self.__acervo.append(Item)
    
    def RemoverMaterial(self, Item):
        if isinstance(Item, Material) and Item in self.__acervo:
            self.__acervo.remove(Item)

    def EmprestarMaterial(self, Item, Consultor):
        if isinstance(Item, Material) and isinstance(Consultor, Usuario):
            if Item in self.__acervo and Item.getDisponibilidade():
                Item.setDisponibilidade(False)
                Consultor.PegarEmprestado(Item)
                
            elif Item in self.__acervo and not Item.getDisponibilidade():
                print('Item Indisponivel')

            else:
                print('Item nao está presente no acervo')
        else:
            print('Erro na consulta do Item')

    def DevolverMaterial(self, Item, Retorno):
        if isinstance(Retorno, Usuario) and isinstance(Item, Material):
            if Item not in self.__acervo:
                print("Este Item nao pertence ao acervo")
            elif Item.getTitulo() not in Retorno.getInventario():
                print(f'O usuario {Retorno.getNome()} nao está com esse Item')
            else:
                Retorno.DevolverItem(Item)
                Item.setDisponibilidade(True)
                print(f'Item {Item.getTitulo()} devolvido com sucesso por {Retorno.getNome()}')
        else:
            print('Erro na operação de Retorno')

    def ConsultarAcervo(self):
        lista_livros = []
        lista_revistas = []

        for i in self.__acervo:
            if isinstance(i, Revista):
                lista_revistas.append(i)
            if isinstance(i, Livro):
                lista_livros.append(i)
        
        print(' ====== Revistas no acervo ====== ')
        if len(lista_revistas) != 0:
            for i in lista_revistas:
                print()
                i.ExibirInfo()
                print()
                print(' ================================== ')
        else:
            print('Vazio')
        
        print()
        print(' ====== Livros no acervo ====== ')

        if len(lista_livros) != 0:
            for i in lista_livros:
                print()
                i.ExibirInfo()
                print()
                print(' ================================== ')
        else:
            print('Vazio')