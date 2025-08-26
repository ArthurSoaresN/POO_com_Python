# CLASSE FILHA CONTA CORRENTE
from conta import Conta
import random

LIMITE = 15000

class ContaCorrente(Conta):
    def __init__(self, nome_cliente: str, numero_conta: int, saldo: float, limite_especial: int):
        super().__init__(nome_cliente, numero_conta, saldo)

        if limite_especial <= LIMITE:
            self.__limite_especial = limite_especial
        else:
            raise ValueError('O limite especial maximo é de 15000')
        
        ContaCorrente.GerarCodigo(self)
        
    def GerarCodigo(self):
        codigo_gerado = random.randint(1,9999)
        self.__codigo_conta = codigo_gerado

    # GET 

    def getLimite(self):
        return self.__limite_especial
    
    def getCodigo(self):
        return self.__codigo_conta
    
    # SET

    def setLimite(self, novo_limite):

        if novo_limite > 15000:
            raise ValueError('O limite precisa ser no maximo de 15000')
        else:
            self.__limite_especial = novo_limite

    # METODOS
    
    def imprimir(self):
        super().imprimir()
        print(f'Limite da Conta: {self.__limite_especial}')
        print(f'Codigo da Conta: {self.__codigo_conta}')

    def depositar(self, valor_depositado):
        
        if not isinstance(valor_depositado, float):
            raise TypeError('O valor depositado precisa ser float')
        if valor_depositado <= 0.0:
            raise ValueError('O valor depositado precisar ser mais que 0')
       
        deposito = ContaCorrente.getSaldo(self) + valor_depositado
        ContaCorrente.setSaldo(self, deposito)

    


    def sacar(self, valor_sacado):

        if valor_sacado > self.__saldo:
            raise ValueError('O valor sacado nao pode ser maior que o Saldo')
        if not isinstance(valor_sacado, float):
            raise TypeError('O valor sacado precisa ser float')
        if valor_sacado <= 0.0:
            raise ValueError('O valor sacado precisa ser maior que 0')
        
        saque = ContaCorrente.getSaldo - valor_sacado
        ContaCorrente.setSaldo(self, saque)