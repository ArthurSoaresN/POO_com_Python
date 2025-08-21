# representar o usuário da biblioteca
# Métodos: pegar_emprestado(material), devolver(material) e consultar_historico()

from material import Material

class Usuario:
    def __init__(self, nome: str, id: int):
        self.__nome = nome
        self.__id = id
        self.__historico = []
        self.__inventario = []

    # GET

    def getNome(self):
        return self.__nome
    
    def getId(self):
        return self.__id
    
    def getHistorico(self):
        LenHistorico = len(self.__historico)
        if LenHistorico != 0:
            return self.__historico
        
    def getInventario(self):
        return self.__inventario
    
    # SET
    
    def setInventario(self, novo_inventario: list):
        self.__inventario = novo_inventario

    def setNome(self, novo_nome: str):
        self.__nome = novo_nome
    
    def setId(self, novo_id: int):
        self.__id = novo_id

    # METODOS

    def PegarEmprestado(self, Item: Material):
        self.__historico.append(Item.getTitulo)
        self.__inventario.append(Item.getTitulo)

    def DevolverItem(self, Item: Material):
        self.__inventario.remove(Item.getTitulo)
    
    def MostrarHistorico(self):
        LenHistorico = len(self.__historico)

        if LenHistorico != 0:
            print(f"Historico do usuario {self.__nome}: ")
            for i in self.__historico:
                print(f'{i}. {self.__historico[i]}')
        else:
            print(f"Historico do usuario {self.__nome} vazio")

