from conta import Conta

conta1 = Conta("Anthony", 1)
try:
    conta1.setFlag(True)
except Exception as erro:
    print(erro)

conta2 = Conta("Will", 2)
try:
    conta2.setFlag(True)
except Exception as erro:
    print(erro)


conta3 = Conta("Edson", 3)

nome_conta1 = conta1.getNome()
print(nome_conta1)

try:
    conta1.setNome(123)
except Exception as erro:
    print(erro)
    
numero_conta1 = conta1.getNumeroConta()
print(numero_conta1)

saldo_conta1 = conta1.getSaldo()
print(saldo_conta1)

try:
    conta3.depositar(100.00)
except Exception as erro:
    print(erro)

sucesso = False

while not sucesso:
    print("Informe o valor que deseja depositar:")
    valor = input()
    try:
        valor = float(valor)  # converte string para float
        conta1.depositar(valor)
        sucesso = True
    except Exception as erro:
        print(f"Erro: {erro}")

