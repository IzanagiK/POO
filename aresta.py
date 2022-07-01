class Aresta:
    def __init__(self, origem, destino):
        self.__origem = origem
        self.__destino = destino
    
    def __str__(self):
        return self.__origem, self.__destino
        
    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self, origem):
        self.__origem = origem
        
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, destino):
        self.__destino = destino