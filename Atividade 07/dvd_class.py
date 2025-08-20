from item import Item

# diretor

# Classe filha
class DVD(Item):
    def __init__ (self, _titulo: str, _tempo: int, _diretor: str, _possuir: bool, _comentario: str):
        super().__init__(_titulo, _tempo, _possuir, _comentario)
        self._diretor = _diretor

     # IMPRIMIR ATRIBUTOS

    def imprimi(self):
        super().imprimi()
        print(f"Diretor: {self._diretor}")

    # Metodos de acessar e modificar

    # DIRETOR

    def getArtista(self):
        return self._diretor
    
    def setArtista(self, novo_diretor: str):
        self._diretor = novo_diretor

    
                
    

