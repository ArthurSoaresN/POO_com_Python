# Programa principal

from material import Material
from livro import Livro
from revista import Revista
from usuario import Usuario
from biblioteca import Biblioteca

AcervoBiblioteca = []
UsuariosBiblioteca = []

def criar_usuario(nome_de_usuario: str):
    identidade = len(UsuariosBiblioteca) + 1
    novo_usuario = Usuario(nome_de_usuario, identidade)
    UsuariosBiblioteca.append(novo_usuario)
    return novo_usuario
    
def adicionar_livro(titulo_livro: str, origem_livro: str, ano_livro: int, disponibilidade: bool, genero: str, paginas: int):
    novo_livro = Livro(titulo_livro, origem_livro, ano_livro, disponibilidade, genero, paginas) 
    AcervoBiblioteca.append(novo_livro)
    return novo_livro

def adicionar_revista(titulo_revista: str, origem_revista: str, ano_revista: int, disponibilidade: bool, edicao: str):
    nova_revista = Revista(titulo_revista, origem_revista, ano_revista, disponibilidade, edicao)
    AcervoBiblioteca.append(nova_revista)
    return nova_revista

usuario1 = criar_usuario('Jose')
usuario2 = criar_usuario('Marcia')
usuario3 = criar_usuario('Davi Brito')
usuario4 = criar_usuario('Alan')
usuario5 = criar_usuario('Neymar')

print()
id1 = usuario1.getId()
nome1 = usuario1.getNome()
print(nome1)
print(id1)


revista1 = adicionar_revista("Plano T", "Veja", 2025, True, "2934")
revista2 = adicionar_revista("The Cruel Kid's Table", 'New York', 2025, True, "Edition")
revista3 = adicionar_revista("UM CHEFE DE GOVERNO", 'Oeste', 2025, True, "479")
revista4 = adicionar_revista('PSICOSE', 'Oeste', 2024, True, '236')

print()
revista3.ExibirInfo()




biblioteca = Biblioteca(AcervoBiblioteca, UsuariosBiblioteca)

