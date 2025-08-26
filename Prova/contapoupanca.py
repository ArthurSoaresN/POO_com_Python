# CLASSE FILHA CONTA POUPANCA

from conta import Conta
import random

class ContaPoupanca(Conta):
    def __init__(self, nome_cliente: str, numero_conta: int, saldo: float, indice_mensal: float):
        super().__init__(nome_cliente, numero_conta, saldo)

        self.__indice_mensal = indice_mensal
        self.__variacao = random.randint(1,10)
        self.__saldo_disponivel = 0.0

    # GET

    def getIndice(self):
        return self.__indice_mensal
    
    def getVariacao(self):
        return self.__variacao
    
    def getSaldoDisponivel(self):
        return self.__saldo_disponivel


    # SET

    def setIndice(self, novo_indice):

        if not isinstance(novo_indice, float):
            raise TypeError('O indice precisa ser float')
        elif novo_indice <= 0.0:
            raise ValueError('O indice precisa ser maior que 0')
        else:
            self.__indice_mensal = novo_indice
    
    def setSaldoDisponivel(self, novo_saldo):
        self.__saldo_disponivel = novo_saldo

    # METODOS

    def imprimir(self):
        super().imprimir()
        print(f'Variacao: {self.__variacao}')
        print(f'Indice da conta: {self.__indice_mensal}')

    def CalcularSaldo(self):

        if not isinstance(self.__indice_mensal, float):
            raise TypeError('O indice precisa ser float')
        else:
            conta =  self.__saldo * self.__indice_mensal
            ContaPoupanca.setSaldoDisponivel(self, conta)
