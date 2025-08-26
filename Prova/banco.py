# CLASSE BANCO

from conta import Conta
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca



class Banco:
    def __init__(self, lista_contas: list):
        self.__lista_contas = lista_contas
    
    
    def InserirConta(self, Usuario):
        
        if isinstance(Usuario, Conta):
            self.__lista_contas.append(Usuario)
    
    def RemoverConta(self, Usuario):

        if not Usuario in self.__lista_contas:
            raise TypeError('O Usuario nao esta na lista')
        
        if isinstance(Usuario, ContaPoupanca) or isinstance(Usuario, ContaCorrente):
            self.__lista_contas.remove(Usuario)
    
    def VerificarListaVazia(self):

        if len(self.__lista_contas) == 0:
            return True
        else:
            return False
        
    def ImprimirContas(self, lista_contas):

        lista_poupanca = []
        lista_corrente = []

        if Banco.VerificarListaVazia(self):
            print('Nao ha contas')
        else:
            for i in lista_contas:
                if isinstance(i, ContaPoupanca):
                    lista_poupanca.append(i)
                if isinstance(i, ContaCorrente):
                    lista_corrente.append(i)
            print()   
            print(' ========= Lista das contas correntes: =========')
            for i in lista_corrente:
                print()
                i.imprimir()
            print()
            print(' ========= Lista das contas poupancas: =========')   
            for i in lista_poupanca:
                print()
                i.imprimir()

    def VerificarNumero(self, numero):

        if Banco.VerificarListaVazia(self):
            print('Lista Vazia')
        else:

            for i in self.__lista_contas:
                if i.getConta() == numero:
                    return True
            else: 
                return False
        
