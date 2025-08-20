# Classe conta
# atributos privados: Nome do correntista, numero da conta, saldo disponivel
# flag informando se a conta está ativa ou não. 

# O construtor inicia o nome do correntista, numero da conta atraves
# de paramentros, outros atributos devem ser atribuidos. (Saldo e flag)

# Metodos: Saque e deposito
# Dinheiro é sempre positivo e só é possivel fazer saques se houver saldo
# Caso contrário tratar com exceções nos proprios metodos

# Get e Set para atributos pois são privados. Verificar necessidade
# de execeções nesses metodos

# Testar tudo na main
# Tentar recuperar erros usando laços. Por exemplo
# Saldo indisponivel. tente novamente
# Valor inválido. tente novamente



class Conta:
    def __init__(self, NomeCorrentista: str, NumeroConta: int):
        self.__NomeCorrentista = NomeCorrentista
        self.__NumeroConta = NumeroConta
        self.__SaldoDisponivel = 0.0
        self.__Flag = False

    # Metodos Get e Set

    def getNome(self):
        return self.__NomeCorrentista

    def setNome(self, NovoNome):
        if not isinstance(NovoNome, (str)):
            raise TypeError("Nome Invalido")
        else:
            self.__NomeCorrentista = NovoNome
            return self.__NomeCorrentista
    
    def getNumeroConta(self):
        return self.__NumeroConta

    def setNumeroConta(self, NovoNumero):
        if not isinstance(NovoNumero, (int)):
            raise TypeError("Numero Invalido")
        else:
            self.__NumeroConta = NovoNumero
            return self.__NumeroConta
    
    def getSaldo(self):
        return self.__SaldoDisponivel
    
    def setSaldo(self, NovoSaldo):
        if not isinstance(NovoSaldo, (float)):
            raise TypeError("Valor Invalido")
        else:
            self.__SaldoDisponivel = NovoSaldo
            return self.__SaldoDisponivel
    
    def getFlag(self):
        return self.__Flag
    
    def setFlag(self, NovoValor):
        if not isinstance(NovoValor, (bool)):
            raise TypeError("Valor de Flag Invalida")
        else:
            self.__Flag = NovoValor
            return self.__Flag
        
    # Metodos

    def depositar(self, valor_depositado):
        if not self.__Flag:
            raise TypeError("Conta Inativa")
        if not isinstance(valor_depositado, (float)):
            raise TypeError("Valor do depósito deve ser type float")
        if valor_depositado <= 0.0:
            raise ValueError("Valor do depósito deve ser maior que zero")  
        
        self.__SaldoDisponivel += valor_depositado
    
    def sacar(self, valor_solicitado):
        if not self.__Flag:
            raise TypeError("Conta Inativa")
        if not isinstance(valor_solicitado, (float)):
            raise TypeError("Valor do saque deve ser type float")
        if valor_solicitado > self.__SaldoDisponivel:
            raise ValueError("Valor solicitado maior que o saldo na conta")
        if valor_solicitado <= 0.0:
            raise TypeError("Valor do saque deve ser maior que zero")
        
        self.__SaldoDisponivel -= valor_solicitado

