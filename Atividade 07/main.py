# Importando as classes necessárias
from cd_class import CD
from dvd_class import DVD
from item import Item
from catologo_class import Catalogo
from typing import Union

def main():
    
    catalogo = Catalogo()
 
    cd1 = CD("Album X", 60, "Artista A", True, "Muito bom!")
    cd2 = CD("Album Y", 45, "Artista B", False, "Não gostei muito.")
    dvd1 = DVD("Filme Z", 120, "Diretor A", True, "Muito emocionante!")
    dvd2 = DVD("Filme W", 150, "Diretor B", False, "Um pouco longo.")

    catalogo.adicionar_item(cd1)
    catalogo.adicionar_item(cd2)
    catalogo.adicionar_item(dvd1)
    catalogo.adicionar_item(dvd2)

    catalogo.listar_item() 

    teste = catalogo.esta_vazio()
    print(teste)
   
    procurar = catalogo.verificar_item("Album X")
    print(procurar)
        
    posse = catalogo.verificar_posse("Filme Z")
    print(posse)
        
    catalogo.listar_meus_itens()

    catalogo.remover_item(cd2)
    catalogo.listar_item()

    teste2 = catalogo.verificar_item("Album Y")
    print(teste2)
   
    vazio = catalogo.esta_vazio()
    print(vazio)
       

if __name__ == "__main__":
    main()
