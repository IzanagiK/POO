from vertice import Vertice
from aresta import Aresta

class Grafo:
    def __init__(self):
        self.__vertices = list()
        self.__arestas = list()
        self.makeRoot()
        
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
        
    def getVertice(self, url):
        for vertice in self.__vertices:
            if vertice.url == url:
                return vertice
        return None

    def getVerticeURL(self, url):
        for vertice in self.__vertices:
            if vertice.url == url:
                return vertice.url
        return None
    
    def getVerticeIP(self, url):
        for vertice in self.__vertices:
            if vertice.url == url:
                return vertice.ip
        return None

    #Exemplo de função que imprime as ligações do grafo
    def getArestas(self):
        s = ''
        for a in self.__arestas:
            s += (a.origem.url + '->' + a.destino.url) + '\n'
        return s
    
    def listVertices(self):
        s = ''
        for a in self.__vertices:
            s += (a.url + '->' + a.ip) + '\n'
        return s

    
    #Trevessia BFS: atravessa todo o grafo até achar o vertice
    def match(self, url):
        for vertice in self.__vertices:
            vertice.visitado = False
        
        fila = list()
        inicio = self.getVertice('/')
        if inicio is not None:
            inicio.visitado = True
            fila.append(inicio)
            indice = 0
            tamanhoURL = len(url) - 1
            while len(fila) != 0:
                verticeTmp = fila.pop()
                if indice == tamanhoURL:
                    return controle
                for aresta in verticeTmp.vizinhos:
                    w = aresta.destino
                    if w.visitado == False:
                        if w.url == url[indice]:
                            controle = True
                            indice += 1
                        else:
                            controle = False
                        w.visitado = True
                        fila.append(w)
            return controle

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