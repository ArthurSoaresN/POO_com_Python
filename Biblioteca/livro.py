# Classe Filha Livro
# Livro herda de Material. Atributos adicionais: genero e numero_paginas.

from material import Material

class Livro(Material):
    def __init__(self, titulo, origem, ano, disponibilidade, genero: str, paginas: int):
        super().__init__(titulo, origem, ano, disponibilidade)
        self.__genero = genero
        self.__paginas = paginas

    # METODOS GET

    def getGenero(self):
        return self.__genero
    
    def getPaginas(self):
        return self.__paginas
    
    # METODOS SET

    def setGenero(self, novo_genero: str):
        self.__genero = novo_genero
    
    def setPaginas(self, novo_paginas: int):
        self.__paginas = novo_paginas
    
    # Metodo

    def ExibirInfo(self):
        super().ExibirInfo()
        print(f'Genero: {self.__genero}')
        print(f'Numero de Paginas: {self.__paginas}')