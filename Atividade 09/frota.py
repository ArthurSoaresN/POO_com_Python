from carro import Carro
from bicicleta import Bicicleta
from moto import Moto
from veiculo import Veiculo

class Frota:

    def __init__(self):
        self.__frota = []

    def adicionar_veiculo(self, veiculo):
        testar_veiculo = 0

        if (isinstance(veiculo, Carro)) or (isinstance(veiculo, Moto)) or (isinstance(veiculo, Bicicleta)):
            testar_veiculo = 1

        if testar_veiculo:
            self.__frota.append(veiculo)
    
    def remover_veiculo(self, veiculo):
        testar_veiculo = 0

        if (isinstance(veiculo, Carro)) or (isinstance(veiculo, Moto)) or (isinstance(veiculo, Bicicleta)):
            testar_veiculo = 1

        if testar_veiculo and veiculo in self.__frota:
            self.__frota.remove(veiculo)

    def remover_moto(self, veiculo):
        testar_moto = isinstance(veiculo, Moto)

        if testar_moto and veiculo in self.__frota:
            self.__frota.remove(veiculo)
    
    def esta_vazia(self):
        return len(self.__frota) == 0
    
    def procurar_motos(self):
        for i in self.__frota:
            if isinstance(i, Moto):
                return True
        return False
    
    def procurar_veiculo(self, modelo_veiculo: str):
        for i in self.__frota:
            if i.getModelo() == modelo_veiculo:
                return True
        return False

    def procurar_carro(self, modelo_carro: str):
        for i in self.__frota:
            if isinstance(i, Carro) and (i.getModelo() == modelo_carro):
                return True
        return False
    
    def imprime_frota(self):
        carros = []
        motos = []
        bicicletas = []

        for veiculo in self.__frota:
            if isinstance(veiculo, Carro): 
                carros.append(veiculo)
            elif isinstance(veiculo, Moto):
                motos.append(veiculo)
            elif isinstance(veiculo, Bicicleta):
                bicicletas.append(veiculo)
        
        if carros:
            print("Carros na frota:")
            for i in carros:
                i.imprime()  # Corrigido

        if motos:
            print("Motos na frota:")
            for i in motos:
                i.imprime()

        if bicicletas:
            print("Bicicletas na frota:")
            for i in bicicletas:
                i.imprime()
