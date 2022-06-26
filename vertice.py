from aresta import Aresta


class Vertice:
    def __init__(self, url, ip):
        self.__url = url
        #self.__ip = ip
        self.__vizinhos = list()
        self.visitado = False
    
    def __str__(self):
        return f'self.__url', f'self.__ip'
    
    def addVizinhos(self, ligacao: Aresta):
        self.__vizinhos.append(ligacao)
    
    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, url):
        self.__url = url
        
    '''@property
    def ip(self):
        return self.__ip
    
    @ip.setter
    def url(self, ip):
        self.__ip = ip'''
        
    @property
    def vizinhos(self):
        return self.__vizinhos
    
    @vizinhos.setter
    def vizinhos(self, vizinhos):
        self.__vizinhos = vizinhos