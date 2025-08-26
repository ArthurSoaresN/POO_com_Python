# CLASSE MAIN BANCO

from banco import Banco
from conta import Conta
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca

lista_usuarios = []
banco = Banco(lista_usuarios)

print('Verificao antes de adicionar usuarios')
teste1 = banco.VerificarListaVazia()
print(f'Esta Vazia? {teste1}')


usuario1 = ContaCorrente('Jose', 10, 100.0, 10000)
usuario2 = ContaCorrente('Jorge', 11, 200.0, 100)
usuario3 = ContaCorrente('Janio', 12, 300.0, 10)

usuario4 = ContaPoupanca('Maria', 1, 10.0, 0.5)
usuario5 = ContaPoupanca('Marcos', 2, 20.0, 0.8)
usuario6 = ContaPoupanca('Marcia', 3, 30.0, 0.2)

banco.InserirConta(usuario1)
banco.InserirConta(usuario2)
banco.InserirConta(usuario3)
banco.InserirConta(usuario4)
banco.InserirConta(usuario5)
banco.InserirConta(usuario6)

print('Verificao depois de adicionar usuarios')
teste2 = banco.VerificarListaVazia()
print(f'Esta Vazia? {teste2}')

# TESTANDO IMPRESSAO
print()
banco.ImprimirContas(lista_usuarios)


print()
verificar1 = banco.VerificarNumero(10)
print('Procurando o usuario de codigo 10')
print(10)

print('Procurando usuario que nao existe:')
verificar2 = banco.VerificarNumero(77)
print(verificar2)

# TESTAR REMOVER CONTA

print("Conta Removida")
banco.RemoverConta(usuario4) # CONTA REMOVIDA
verificar3 = banco.VerificarNumero(1) # PROCURAR CONTA -> FALSE
print(f'Procurando conta removida resultado: {verificar3}')


tentativa = True

while tentativa:
    try:
        banco.RemoverConta(usuario5)
        tentativa = False
    except Exception as erro:
        print(f'Erro: {erro}')
        print('Tente novamente')
        exit()

