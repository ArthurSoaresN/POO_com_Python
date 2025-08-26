# CLASSE PAI

class Conta:
    def __init__(self, nome_cliente: str, numero_conta: int, saldo: float):
        self.__nome_cliente = nome_cliente
        self.__numero_conta = numero_conta
        self.__saldo = saldo
    
    # GET

    def getNome(self):
        return self.__nome_cliente

    def getConta(self):
        return self.__numero_conta
    
    def getSaldo(self):
        return self.__saldo
    
    # SET

    def setNome(self, novo_nome):

        if not isinstance(novo_nome, str):
            raise TypeError('O nome precisa ser string')

        self.__nome_cliente = novo_nome
    
    def setNumero(self, novo_numero):

        if not isinstance(novo_numero, int):
            raise TypeError('O numero precisa ser int')

        self.__numero_conta = novo_numero
    
    def setSaldo(self, novo_saldo):

        if not isinstance(novo_saldo, float):
            raise TypeError('O saldo precisa ser float')
        
        self.__saldo = novo_saldo

    # METODO 

    def imprimir(self):
        print(f'Nome do Cliente: {self.__nome_cliente}')
        print(f'Numero da Conta: {self.__numero_conta}')
        print(f'Saldo da Conta: {self.__saldo}')
