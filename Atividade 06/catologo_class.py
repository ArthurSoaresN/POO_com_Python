# Permitir a inserção de informações sobre CDs - FEITO
# Permitir que se removam CDs - FEITO
# Listar todos os CDs com suas informações - FEITO
# Verificar se há ou não CDs no catálogo, isto é, catálogo vazio - FEITOS
# Verificar se há um determinado CD no catálogo, verificação pelo atributo. Se houver, imprimir as informações - FEITO
# Verificar se possuo determinado CD. Se possuir, imprimir as informações - FEITO
# Listar todos os CDs que possuo com suas informações

from cd_class import CD

class Catalogo:
    
    def __init__(self):
        self._cds = []
        
    def adicionar_cd(self, cd: CD):
        self._cds.append(cd)

    def remover_cd(self, cd: CD):
        self._cds.remove(cd)
  
    def listar_cds(self):
        tamanho_lista = len(self._cds)
        for i in range(tamanho_lista):
            self._cds[i].imprimi()

    def esta_vazio(self):
        return len(self._cds) == 0
    
    def verificar_cd(self, titulo: str, artista: str):
        for cd in self._cds:
            if cd.getTitulo() == titulo and cd.getArtista() == artista:
                cd.imprimi()
                return True
            else:
                return False
                
    
    def verificar_posse(self, titulo: str):
        for cd in self._cds:
            if cd.getTitulo() == titulo:
                if cd.getPossuir() == True:
                    return True
                else:
                    return False

    def listar_meus_cds(self):
        tamanho_lista = len(self._cds)
        for i in range(tamanho_lista):
            if self._cds[i].getPossuir() == 1:
                self._cds[i].imprimi()