from Browser import *
import os

usuario = Browser()
print("Bem-vindo ao sistema de simulação de BROWSER - Insira uma url para ser carregada ou digite #help para ver a lista de comandos")
while True:
    busca = input('Search:')
    os.system('cls')
    
    if busca == '#sair':
        break
    else:
        usuario.buscar(busca)
        
    usuario.printHistorico()
    usuario.printHome()