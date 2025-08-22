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

print(' ====== Exibindo uma Revista ====== ')
revista3.ExibirInfo()
print(' ================================== ')

livro1 = adicionar_livro('O manifesto do partido Comunista', 'Boitempo', 1848, True, 'Economia', 254)
livro2 = adicionar_livro('As seis licoes', 'LVM', 1959, True, 'Economia', 184)
livro3 = adicionar_livro('O principe', 'Garnier', 1513, True, 'Politica', 96)
livro4 = adicionar_livro('A Revolução dos Bichos', 'Garnier', 1945, True, 'Fantasia', 96)

print(' ====== Exibindo um Livro ====== ')
livro1.ExibirInfo()
print(' ================================== ')

biblioteca = Biblioteca(AcervoBiblioteca, UsuariosBiblioteca)

# biblioteca.ConsultarAcervo() # Consultando acervo


biblioteca.EmprestarMaterial(revista3, usuario1)



print(' ====== Revista Pos Emprestimo ====== ')
revista3.ExibirInfo()
print(' ================================== ')

print(' ====== Historico do Usuario que pegou o livro ====== ')
usuario1.MostrarHistorico()
print(' ================================== ')