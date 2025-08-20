from cd_class import CD
from catologo_class import Catalogo

def main():
    # Criando 4 CDs com dados fictícios de músicas brasileiras
    cd1 = CD("Evidencias", 240, "Chitãozinho & Xororo", True, "Clássico sertanejo")

    cd2 = CD("Pais e Filhos", 290, "Legião Urbana", False, "Rock nacional")

    cd3 = CD("Ai Se Eu Te Pego", 210, "Michel Telo", True, "Hit internacional")

    cd4 = CD("Aquarela", 300, "Toquinho", False, "Música calma")

    # Testando métodos individuais da classe CD
    print("=== Testando atributos individuais dos CDs ===")
    cd1.imprimi()
    cd2.imprimi()
    cd3.imprimi()
    cd4.imprimi()

    # Criando catálogo
    catalogo = Catalogo()

    # Adicionando CDs ao catálogo
    catalogo.adicionar_cd(cd1)
    catalogo.adicionar_cd(cd2)
    catalogo.adicionar_cd(cd3)
    catalogo.adicionar_cd(cd4)

    # Removendo CD

    catalogo.remover_cd(cd4)

    # Listar todos os CDs
    print("\n=== Listar todos os CDs ===")
    catalogo.listar_cds()

    # Verificar se catálogo está vazio
    print("\n=== Verificar se catálogo está vazio ===")
    TesteVazio = catalogo.esta_vazio()
    print(TesteVazio)

    # Verificar se há um CD específico no catálogo
    print("\n=== Verificar se existe um CD específico ===")
    TesteVerificar1 = catalogo.verificar_cd("Pais e Filhos", "Legião Urbana")
    TesteVerificar2 = catalogo.verificar_cd("Não Existe", "Artista Qualquer")
    print(TesteVerificar1)
    print(TesteVerificar2)


    # Verificar se possuo determinado CD
    print("\n=== Verificar posse de CDs ===")
    Teste = catalogo.verificar_posse("Ai Se Eu Te Pego")
    print(Teste)
   

    # Listar apenas os CDs que possuo
    print("\n=== Listar meus CDs ===")
    catalogo.listar_meus_cds()

    # Remover um CD e listar novamente
    print("\n=== Remover um CD e listar novamente ===")
    catalogo.remover_cd(cd2)
    catalogo.listar_cds()

if __name__ == "__main__":
    main()

