from vertice import Vertice
from aresta import Aresta

class Grafo:
    def __init__(self):
        self.__vertices = list()
        self.__arestas = list()
        
    def __str__(self):
        return f'self.arestas', f'self.vertices'
        
    def makeRoot(self):
        raiz = self.addVertice('/','0.0.0.0')
        return raiz
    
    def addVertice(self, url, ip):
        newVertice = Vertice(url,ip)
        self.vertices.append(newVertice)
        return newVertice
        
    def addAresta(self, origem: 'Vertice', destino: 'Vertice'):
        caminho = Aresta(origem, destino)
        origem.addVizinhos(caminho)
        self.__arestas.append(caminho)
        return caminho
        
    def getVertice(self, pesquisa):
        for vertice in self.__vertices:
            if vertice.url == pesquisa:
                return vertice
        return None
    
    #Trevessia BFS: atravessa todo o grafo até achar o vertice
    def bfs(self, pesquisa):
        for vertice in self.__vertices:
            vertice.visitado = False
        
        fila = list()
        inicio = self.getVertice('teste')
        if inicio is not None:
            inicio.visitado = True
            fila.append(inicio)
            while len(fila) != 0:
                verticeTmp = fila.pop()
                for aresta in verticeTmp.vizinhos:
                    w = aresta.destino
                    if w.visitado == False:
                        if w.url == pesquisa:
                            print(w.url)
                        w.visitado = True
                        fila.append(w)        
    
    def match(self, pesquisa):
        pass
        
    #getter & setters        
    @property
    def vertices(self):
        return self.__vertices
    
    @vertices.setter
    def vertices(self, vertices):
        self.__vertices = vertices
        
    @property
    def arestas(self):
        return self.__arestas
    
    @arestas.setter
    def arestas(self, arestas):
        self.__arestas = arestas

        
'''teste = Grafo()
v1 = teste.addVertice('teste')
v2 = teste.addVertice('teste2')
teste.addAresta(v1,v2)
v3 = teste.addVertice('teste3')
v4 = teste.addVertice('teste4')
teste.addAresta(v1,v3)
teste.addAresta(v3,v4)

teste.bfs('teste5')'''