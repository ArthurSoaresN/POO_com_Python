import random # Para trilhas
from item import Item

#artista
#trilhas

# Classe filha

class CD(Item):
    def __init__ (self, _titulo: str, _tempo: int, _artista: str, _possuir: bool, _comentario: str):
        super().__init__(_titulo, _tempo, _possuir, _comentario)
        self._artista = _artista
        self._trilhas = self.__numero_de_trilhas()

    # TRILHAS

    def __numero_de_trilhas(self):
        numeros = random.randint(0, 20)
        return numeros

    def getTrilha(self):
        return self.__numero_de_trilhas

    # IMPRIMIR ATRIBUTOS

    def imprimi(self):
        super().imprimi()
        print(f"Artista: {self._artista}")
        print(f"Trilha: {self._trilhas}")
    
    # Metodos de acessar e modificar

    # ARTISTA

    def getArtista(self):
        return self._artista
    
    def setArtista(self, novo_artista: str):
        self._artista = novo_artista

 
    
                
    

