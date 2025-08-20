from bicicleta import Bicicleta
from carro import Carro
from frota import Frota
from moto import Moto
from veiculo import Veiculo

frota = Frota()

bicicleta = Bicicleta("Modelo 1", "Caloi", 2, "Boa bicicleta", 6)
print(bicicleta)

bicicleta2 = Bicicleta("Modelo 2", "Monark", 2, "Boa bicicleta", 6)

carro = Carro("Corola", "Toyota", 4, "Excelente carro", 4)
carro2 = Carro("HB20", "Hyundai", 4, "Excelente carro", 4)

moto = Moto("Pop", "Honda", 2, "Muito economica", 110)
moto2 = Moto("Titan", "Honda", 2, "Bom custo beneficio", 125)

# Inserção
frota.adicionar_veiculo(bicicleta) 
frota.adicionar_veiculo(bicicleta2)
frota.adicionar_veiculo(carro)  
frota.adicionar_veiculo(carro2)
frota.adicionar_veiculo(moto)
frota.adicionar_veiculo(moto2)

# Remoções
frota.remover_veiculo(bicicleta2)
frota.remover_moto(moto2)
frota.remover_moto(bicicleta)  # Teste: não deve remover nada

# Consultas
eh_vazia = frota.esta_vazia()
print(f"Frota está vazia? {eh_vazia}")

tem_moto = frota.procurar_motos()
print(f"Há motos na frota? {tem_moto}")

buscar_carro = frota.procurar_carro("HB20")
print(f"Carro HB20 encontrado? {buscar_carro}")

# Impressão
frota.imprime_frota()
