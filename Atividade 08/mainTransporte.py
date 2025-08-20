from veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta

bicicleta = Bicicleta("Modelo 1", "Caloi", 2, "Boa bicicleta", 6)
carro = Carro("Corola","Honda", 4, "Excelente carro", 4)
moto = Moto("Pop", "Honda", 2, "Muito economica", 110)


bicicleta.emite_som()
bicicleta.imprime()
bicicleta.setMarchas(7)
marchas = bicicleta.getMarchas()
print(marchas)

print(" ------------ ")

# SOM, IMPRIME, GET
carro.emite_som()
carro.imprime()
descricao_carro = carro.getDescricao()
print(descricao_carro)

carro.setDescricao("Carro confiavel para viagens")
nova_descricao = carro.getDescricao()
print(nova_descricao)

portas = carro.getPortas()
print(portas)

# SET
carro.setPortas(2)
portas2 = carro.getPortas()
print(portas2)

print(" ------------ ")

moto.emite_som()
moto.imprime()

descricao_moto = moto.getDescricao()
print(descricao_moto)

cilindradas = moto.getCilindradas()
print(cilindradas)

