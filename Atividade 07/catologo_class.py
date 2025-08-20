# Permitir a inserção de informações sobre o item
# Permitir que se removam itens
# Listar todos os itens com suas informações
# Verificar se há ou não itens no catálogo, isto é, catálogo vazio
# Verificar se há um determinado item no catálogo, verificação pelo atributo. Se houver, imprimir as informações
# Verificar se possuo determinado item. Se possuir, imprimir as informações
# Listar todos os itens que possuo com suas informações

from cd_class import CD
from dvd_class import DVD
from item import Item
from typing import Union # Para verificar o tipo

# Verifica se é da class isinstance (objeto, Classe)

class Catalogo:
    
    def __init__(self):
        self._itens = []
        
    def adicionar_item(self, item:Union[CD, DVD]):
         self._itens.append(item)
        
        
    def remover_item(self, item:Union[CD, DVD]):
        self._itens.remove(item)
       
    def listar_item(self):
        if self.esta_vazio():
            print("Lista Vazia")
        
        for i in range(len(self._itens)):
            self._itens[i].imprimi()
        

    def esta_vazio(self):
        return len(self._itens) == 0
    
    def verificar_item(self, titulo: str):
        for item in self._itens:
            if item.getTitulo() == titulo:
                item.imprimi()
                return True
        return False

    def verificar_posse(self, titulo: str):
        for item in self._itens:
            if item.getTitulo() == titulo:
                if item.getPossuir():
                    return True
        return False

    def listar_meus_itens(self):
        cds = [] 
        dvds = [] 

        for item in self._itens:
            if isinstance(item, CD): 
                cds.append(item)
            elif isinstance(item, DVD):
                dvds.append(item)

        if cds:
            print("Lista de CDs:")
            for cd in cds:
                cd.imprimi()

        if dvds:
            print("Lista de DVDs:")
            for dvd in dvds:
                dvd.imprimi()
