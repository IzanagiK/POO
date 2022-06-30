import csv
from Historico import historico
from pilha import Pilha
from grafo import Grafo

'''
Exception para receber e tratar os possíveis erros do programa.
'''
class BrowserException(Exception): #Mensagens de erro da class Browser
    def __init__(self,msg):
        self.msg = msg

class Browser:
    def __init__(self):
        
        '''
        home: Página atual;
        historico: Pilha com o histórico de página acessadas;
        enderecos: Grafo contendo todos os endereços adquiridos através da função
        'importUrls'.
        '''
        
        self.home = None 
        self.historico = Pilha()
        self.enderecos = Grafo()
        self.importUrls()    
    
    def __str__(self):
        return (f'{self.home} {self.historico}')
    
    '''
    Importa os IP's e URL's contidos no arquivo 'ip-url.csv'
    Trata os dados contidos no arquivo e cria um grafo 'enderecos'
    '''
    def importUrls(self):
        dbURL = 'ip-url.csv'
        try:
            with open(dbURL, 'r') as arquivo:
                csv_reader = csv.reader(arquivo, delimiter=';')
                next(csv_reader, None)
                for linha in csv_reader:
                    aresta = self.enderecos.addVertice(linha[1],linha[0])
                    self.enderecos.addAresta(self.enderecos.makeRoot(),aresta)           
                                  
        except FileNotFoundError as fnfe:
            fnfe.BrowserException('Arquivo não encontrado')

    '''
    Recebe os dados a serem procurados no banco de urls.
    '''    
    def buscar(self, url):
            if url == '#help':
                self.help()
            elif url == '#voltar':
                self.back()
            #sessão de testes caso o comando [#help 'comando'] seja acionado
            elif url == '#help add':
                self.helpADD()
            elif url == '#help sair':
                self.helpEXIT()
            elif url == '#help voltar':
                self.helpBACK()
                #sessão de testes caso o comando [#add] seja acionado        
            elif url.startswith('#add'):
                self.addURL(url) 
            elif url == '#voltar':
                self.back()       
            else:
                self.__search(url)

    '''
    Pesquisa em 'enderecos' pela url.
    '''
    def __search(self, url):
        self.addHistory()
        self.home = self.enderecos.getVertice(url)
            
            
    '''
    Adiciona automaticamente ao histórico a última página acessada.
    '''
    def addHistory(self):
        if self.home == None:
            return
        else:
            self.historico.inserir(self.home)

    '''
    Exibe o histórico de páginas acessadas.
    '''
    def printHistorico(self):
        if self.historico.top == None:
            print(f'Páginas Acessadas: []')
        else:
            print(f'Páginas Acessadas: [ {self.historico.imprimir()} ]')
    
    '''
    Exibe a página atual do navegador.
    '''
    def printHome(self):
        if self.home == 'None' or self.home is None:
            print(f'Página Atual: []')
        else:
            print(f'Página Atual: [ {self.home} ]')
        print()

    '''
    Adiciona uma nova URL a lista de urls disponíveis.
    '''    
    def addURL(self, url):
        novo_endereco = url.split()
        novo_endereco = novo_endereco[1].split('/')
        if len(novo_endereco[1]) == 1:
            vertice = self.enderecos.addVertice(novo_endereco[1])
            self.enderecos.addAresta('/',vertice)
        else:
            #Adicionando uma nova Url com subpaginas
            pass

    '''
    Método que printa as funcionalidades de cada comando ao usuário
    '''
    def help(self):
        print('''
            Comandos:
              #add - Adiciona uma nova url no banco de urls.
              #sair - Encerra o programa.
              #voltar - Retorna a página anteriormente acessada.
              #help [comando] - Um help personalizado para cada comando.
              ''')

    def helpADD(self):
        print('Formato: #add www.exemplo.com 1.1.1.1')
    
    def helpEXIT(self):
        print('Encerra o programa. Formato: #sair')
    
    def helpBACK(self):
        print('Retorna a última página acessada antes da página atual (HOME). Formato: #voltar')
    
    '''
    Remove a última página adicionada ao histórico, retornando-a ao campo 'Home'.
    '''    
    def back(self):
        self.home = self.historico.remover()

#teste = Browser()
#print(f'{teste.enderecos.vertices}')
#print()
#print(f'{teste.enderecos.arestas}')

#teste.addURL('#add testando.com 1.1.1.1')