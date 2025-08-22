# Classe Pai

# Atributos:
# Titulo da Revista ou Livro
# Origem Autor ou Editora
# Ano de publicação

# Metodo:
# exibir_informacoes, mostrará quais são os atributos, deve ser implementado com po

class Material:
    def __init__(self, titulo: str, origem: str, ano: int, disponibilidade: bool):
        self.__titulo = titulo
        self.__origem = origem
        self.__ano = ano
        self.__disponibilidade = disponibilidade

    # METODOS GET

    def getDisponibilidade(self):
        return self.__disponibilidade

    def getTitulo(self):
        return self.__titulo
    
    def getOrigem(self):
        return self.__origem
    
    def getAno(self):
        return self.__ano
    
    # METODOS SET

    def setDisponibilidade(self, novo_disponibilidade: bool):
        self.__disponibilidade = novo_disponibilidade

    def setTitulo(self, novo_titulo: str):
        self.__titulo = novo_titulo

    def setOrigem(self, novo_origem: str):
        self.__origem = novo_origem
    
    def setAno(self, novo_ano: int):
        self.__ano = novo_ano

    # Metodo

    def ExibirInfo(self):
        print(f'Titulo: {self.__titulo}')
        print(f'Origem: {self.__origem}')
        print(f'Ano de Postagem: {self.__ano}')
        print(f'Disponibilidade: {self.__disponibilidade}')