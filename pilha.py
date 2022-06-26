class node:
    def __init__(self, dado='', next = None):
        self.dado = dado
        self.next = next
    
    def __repr__(self) -> str:
        return '%s -> %s' % (self.dado, self.next)

class Pilha:
    def __init__(self):
        self.top = None
    
    def __repr__(self):
        return "http://" + str(self.top) + "/"
    
    def inserir(self, novo_dado):
        #cria um novo no com o dado a ser armazenado
        no_novo = node(novo_dado)
        #Faz o novo nó ser o topo da pilha
        no_novo.next = self.top
        #Faz com que a cabeça referencie o novo no
        self.top = no_novo
    
    def remover(self):
        assert self.top, "Impossivel remover algo vazio"
        newHome = self.top
        self.top = self.top.next
        return newHome

        
        
        
        
   