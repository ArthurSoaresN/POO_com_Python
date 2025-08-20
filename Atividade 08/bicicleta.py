from veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, marchas: int):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__marchas = marchas

    # Imprime
    def imprime(self):
        super().imprime()
        print(f"Marchas: {self.__marchas}")

    # METODOS

    def getMarchas(self):
        return self.__marchas
    
    def setMarchas(self, novoMarchas: int):
        self.__marchas = novoMarchas
        return self.__marchas
    
    def emite_som(self):
        print("Bicicleta fazendo barulho...")