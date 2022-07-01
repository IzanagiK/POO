import csv
from Historico import historico
from pilha import Pilha
from grafo import Grafo

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
                    url = linha[1]
                    ip = linha[0]
                    vertice = self.enderecos.addVertice(url, ip)
                    self.enderecos.addAresta(self.enderecos.getVertice('/'), vertice)          
                                  
        except FileNotFoundError as fnfe:
            fnfe.BrowserException('Arquivo não encontrado')

    '''
    Recebe os dados a serem procurados no banco de urls.
    '''    
    def buscar(self, url:str):
        if url == None:
            pass
        else:
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
            #fim da sessão de testes do comando #help       
            elif url.startswith('#add'):
                self.addURL(url) 
            elif url == '#voltar':
                self.back()
            else:
                self.__search(url)

    '''
    Pesquisa em 'enderecos' pela url.
    '''
    def __search(self, url:str):
        newUrl = url.split('/')
        indice = len(newUrl) - 1
        if indice == 0:
            if self.enderecos.getVerticeURL(url) is not None:
                self.addHistory()
                self.home = self.enderecos.getVerticeURL(url)
                print(f'IP: {self.enderecos.getVerticeIP(url)}')
                print('Url encontrada!')
            else:
                print('Url não encontrada')
        elif indice >= 1:
            if(self.enderecos.match(newUrl)):
                self.addHistory()
                self.home = url
                print(f'IP: {self.enderecos.getVerticeIP(newUrl[indice])}')
                print('Url encontrada!')
            else:
                print('Url não encontrada')
            
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
            print(f'Páginas Acessadas: [http:// {self.historico.imprimir()} ]')
    
    '''
    Exibe a página atual do navegador.
    '''
    def printHome(self):
        if self.home is None:
            print(f'Página Atual: []')
        else:
            print(f'Página Atual: [http:// {self.home} ]')
        print()

    '''
    Adiciona uma nova URL a lista de urls disponíveis.
    '''    
    def addURL(self, url:str):
        novo_endereco = url.split()
        subPagina = novo_endereco[1].split('/')
        if len(subPagina) == 1:
            try:
                vertice = self.enderecos.addVertice(novo_endereco[1],novo_endereco[2])
                self.enderecos.addAresta(self.enderecos.getVertice('/'),vertice)
                print('Nova URL adicionada com sucesso!')
            except IndexError:
                print('Comando incompleto, digite "#help add" para verificar a sintaxe do comando!')
        elif len(subPagina) > 1:
            v = subPagina[0]
            if(self.enderecos.getVertice(v) is not None):
                indice = 0
                controle = len(subPagina) - 1
                while indice != controle:
                    try:
                        vertice = self.enderecos.addVertice(subPagina[indice + 1],self.enderecos.getVerticeIP(subPagina[0]))
                        origem = subPagina[indice]
                        self.enderecos.addAresta(self.enderecos.getVertice(origem),vertice)
                        indice += 1
                    except IndexError:
                        pass
                print('Nova URL adicionada com sucesso!')
            else:
                indice = 0
                tamanhoURL = len(subPagina) - 1
                while indice != tamanhoURL:
                    try:
                        vertice = self.enderecos.addVertice(subPagina[indice],novo_endereco[2])
                        if indice == 0:
                            self.enderecos.addAresta(self.enderecos.getVertice('/'),vertice)
                        else:
                            self.enderecos.addAresta(self.enderecos.getArestas(subPagina[indice]),vertice)
                        indice += 1
                    except IndexError:
                        return print('Comando incompleto, digite "#help add" para verificar a sintaxe do comando!')
                print('Nova URL adicionada com sucesso!')

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