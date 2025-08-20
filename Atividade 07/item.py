#Classe Pai

# Construtor
# Metodos de acesso
# Metodos de modificar
# Metodos de imprimir os atributos

# titulo(string) 
# tempo de reprodução(int), 
# possuo(booleano)
# comentário(string)

class Item:
    def __init__ (self, _titulo: str, _tempo: int, _possuir: bool, _comentario: str):
        self._titulo = _titulo
        self._tempo = _tempo
        self._possuir = _possuir
        self._comentario = _comentario
        
     # IMPRIMIR ATRIBUTOS

    def imprimi(self):
        print(f"Titulo: {self._titulo}")
        print(f"Tempo: {self._tempo}")
        print(f"Possui: {self._possuir}")
        print(f"Comentario: {self._comentario}")

    # Metodos de acessar e modificar

    # TITULO

    def getTitulo(self):
        return self._titulo
    
    def setTitulo(self, novo_titulo: str):
        self._titulo = novo_titulo

    # TEMPO

    def getTempo(self):
        return self._tempo

    def setTempo(self, novo_tempo: int):
        self._tempo = novo_tempo

    # POSSUIR
         
    def getPossuir(self):
        return self._possuir
    
    def setPossuir(self, valor_possuir: bool):
        self._possuir = valor_possuir

    # COMENTARIO

    def getComentario(self):
        return self._comentario
    
    def setComentario(self, novo_comentario):
        self._comentario = novo_comentario
