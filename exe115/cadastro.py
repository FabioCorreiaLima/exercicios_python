from time import sleep
from biblioteca.interface import *

while True:
        
    resposta = menu()
    if resposta == 1:
        titulo('Ver pessoas cadastradas')
    elif resposta == 2:
        titulo('Novo cadastro')
    elif resposta == 3:
        titulo('Apagar cadastro')
    elif resposta == 4:
        titulo('Saindo do sistema')
        break
    else:
        print('ERRO! Digite uma opção valida')
        sleep(2)