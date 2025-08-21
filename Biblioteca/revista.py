# Classe Filha Revista
# Revista herda de Material. Atributos adicionais: edicao e mes_publicacao.

from material import Material
import random

MESES = [1,2,3,4,5,6,7,8,9,10,11,12]

class Revista(Material):
    def __init__(self, titulo, origem, ano, disponibilidade, edicao: str):
        super().__init__(titulo, origem, ano, disponibilidade)
        self.__edicao = edicao
        self.__mes = random.randint(1,12)
        

    # METODOS GET

    def getEdicao(self):
        return self.__edicao
    
    def getMess(self):
        return self.__mes
    
    # METODOS SET

    def setEdicao(self, novo_edicao: str):
        self.__edicao = novo_edicao
    
    def setMes(self, novo_mes: int):
        if novo_mes in MESES:
            self.__mes = novo_mes
    
    # Metodo

    def ExibirInfo(self):
        super().ExibirInfo()
        print(f'Edicao: {self.__edicao}')
        print(f'Mes de Postagem: {self.__mes}')