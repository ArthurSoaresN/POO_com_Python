from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, cilindradas: int):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__cilindradas = cilindradas

    # Imprime
    def imprime(self):
        super().imprime()
        print(f"Cilindradas: {self.__cilindradas}")

    # METODOS

    def getCilindradas(self):
        return self.__cilindradas
    
    def setCilindradas(self, novoCilindradas: int):
        self.__cilindradas = novoCilindradas
        return self.__cilindradas

    def emite_som(self):
        print("Moto fazendo barulho...")