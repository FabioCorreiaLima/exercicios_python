
# funcao para ler o arquivo txt
def ler():
    with open(dados, 'rt') as file:
     print(f'NOME     TELEFONE')
     for linha in file: 
        dado = linha.split('\n')
        print(*dado)
         
         
# funcao para validar uma variavel inteira
def Validar_int(msg):
    while True:
        try:
            validar = int(input(f'{msg}'))
        except:
            
            print('\nValor invalido! Digite apenas número inteiro.')
            
        else:
             if len(str(validar)) == 11:
                return validar
             else:
                print('Número de telefone deve conter 11 digitos')
                
                
# funcao para salvar os dados
def salvar(n, t): # recebe o n = nome e t = telefone como argumentos
    with open (dados, mode='at') as arquivo:
        arquivo.write(f'{n:<6}{t:>14}\n')

# arquivo txt
dados = 'contatos.txt'

# Programa principal

while True:
    print('<<< AGENDA TELEFONICA >>>')
    while True:
        nome = input('Nome ou [sair] : ').upper()
        if nome.isalpha():
            break
        else:
            print('Digite apenas números')
    if nome == 'SAIR':
        break
    telefone = Validar_int('Telefone: ')
    salvar(nome, telefone)
    
    ler()
print('<< OBRIGADO >>')