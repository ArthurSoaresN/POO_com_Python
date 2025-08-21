# Classe Pai

# Atributos:
# Titulo da Revista ou Livro
# Origem Autor ou Editora
# Ano de publicação

class Material:
    def __init__(self, titulo: str, origem: str, ano: int):
        self.__titulo = titulo
