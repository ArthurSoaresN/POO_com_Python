# PROGAMA PRINCIPAL PARA TESTAR CONTAS

from conta import Conta
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca

UM_ANO = 12

# CRIANDO USUARIOS
usuario1 = ContaCorrente('Joao', 1, 10.00, 1000)
usuario2 = ContaCorrente('Vinicius', 2, 15.00, 300)

usuario3 = ContaPoupanca('Jorge', 3, 20.00, 0.8)

# IMPRIMINDO USUARIO1
usuario1.imprimir()
print()

# TESTANDO O METODOS
Saldo1 = usuario1.getSaldo()
print(Saldo1)

print()
# TESTANDO ERRO 
try:
    usuario1.depositar(10)
except Exception as erro:
    print(f'Erro: {erro}')
print()

usuario1.depositar(10.0)
print('Pos Deposito:')
usuario1.imprimir()

# TROCANDO ATRIBUTOS POR SET
print()
usuario2.imprimir()
print()
usuario2.setLimite(10000)
usuario2.imprimir()

print()
Indice3 = usuario3.getIndice()
print(Indice3)

calcular_saldo = usuario3.getIndice()
print(calcular_saldo*UM_ANO)

Variacao3 = usuario3.getVariacao()
print(Variacao3)



print()
tentativa = True

while tentativa:
    try:
        print('Digite o valor que deseja depositar')
        valor = input()
        usuario1.depositar(valor)
        tentativa = False
    except Exception as erro:
        print(f'Erro: {erro}')
        