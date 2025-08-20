from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, portas: int):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__portas = portas

    # Imprime
    def imprime(self):
        super().imprime()
        print(f"Portas: {self.__portas}")

    # METODOS

    def getPortas(self):
        return self.__portas
    
    def setPortas(self, novoPortas):
        self.__portas = novoPortas
        return self.__portas
    
    def emite_som(self):
        print("Carro fazendo barulho...")


