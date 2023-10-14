
def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except ( ValueError, TypeError):
            print('ERRO! Digite um número inteiro valido.')
            continue
        else:
            return(n)
        

def linha(tam=42):
    return '-'* tam
    


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    

def menu():
    titulo('CADASTRO DE MORADORES')
    linha()
    print('''
[1] Ver pessoas cadastradas 
[2] Novo cadastro
[3] Apagar cadastro
[4] Sair ''')
    print(linha())
    resposta = leia_int('Opção: ')
    return resposta
    print(linha())
    
    
    
def novo_cadastro():
    nome = str(input)
