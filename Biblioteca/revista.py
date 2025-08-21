# Classe Filha Revista
# Revista herda de Material. Atributos adicionais: edicao e mes_publicacao.

from material import Material

class Revista(Material):
    def __init__(self, titulo, origem, ano, edicao:str, mes:int):
        super().__init__(titulo, origem, ano)
        self.__edicao = edicao
        self.__mes = mes

    # METODOS GET

    def getGenero(self):
        return self.__genero
    
    def getPaginas(self):
        return self.__paginas
    
    # METODOS SET

    def setGenero(self, novo_genero):
        self.__genero = novo_genero
    
    def setPaginas(self, novo_paginas):
        self.__paginas = novo_paginas
    
    # Metodo

    def ExibirInfo(self):
        super().ExibirInfo()
        print(f'Genero: {self.__genero}')
        print(f'Numero de Paginas: {self.__paginas}')