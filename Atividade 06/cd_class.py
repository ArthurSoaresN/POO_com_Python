# Construtor
# Metodos de acesso
# Metodos de modificar
# Metodos de imprimir os atributos

# titulo(string) 
# tempo de reprodução(int), 
# artista(string), 
# numero de trilhas(int) (O número de trilhas deve ser gerado aleatoriamente por um método interno.)
# possuo(booleano)
# comentário(string)

import random # Para trilhas


class CD:
    def __init__ (self, _titulo: str, _tempo: int, _artista: str, _possuir: bool, _comentario: str):
        self._titulo = _titulo
        self._tempo = _tempo
        self._artista = _artista
        self._possuir = _possuir
        self._comentario = _comentario
        self._trilhas = self.__numero_de_trilhas()

    # TRILHAS

    def __numero_de_trilhas(self):
        numeros = random.randint(0, 20)
        return numeros

     # IMPRIMIR ATRIBUTOS

    def imprimi(self):
        atributos = f""" 
        Titulo: {self._titulo}
        Tempo: {self._tempo}
        Artista: {self._artista}
        Possui: {self._possuir}
        Comentario: {self._comentario}
        Trilha: {self._trilhas}
        """
        print(atributos)

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

    # ARTISTA

    def getArtista(self):
        return self._artista
    
    def setArtista(self, novo_artista: str):
        self._artista = novo_artista

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
    
                
    

