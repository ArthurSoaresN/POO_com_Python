class Veiculo:
    def __init__(self, modelo: str, fabricante: str, rodas: int, descricao: str):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__rodas = rodas
        self.__descricao = descricao
        
    # Metodos

    # MODELO

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, novoModelo: str):
        self.__modelo = novoModelo
        return self.__modelo
    
    # FABRICANTE

    def getFabricante(self):
        return self.__fabricante
    
    def setFabricante(self, novoFabricante: str):
        self.__fabricante = novoFabricante
        return self.__fabricante
    
    # RODAS

    def getRodas(self):
        return self.__rodas
    
    def setRodas(self, novoRodas: int):
        self.__rodas = novoRodas
        return self.__rodas
    
    # DESCRICAO

    def getDescricao(self):
        return self.__descricao
    
    def setDescricao(self, novoDescricao):
        self.__drescricao = novoDescricao
        return self.__descricao
    
    # IMPRIMIR

    def imprime(self):
        print(f"Modelo: {self.__modelo}")
        print(f"Fabricante: {self.__fabricante}")
        print(f"Rodas: {self.__rodas}")
        print(f"Descrição: {self.__descricao}")

    def emite_som(self):
        pass

    