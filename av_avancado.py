# Lista avançada
#================================================================================================
#Ex2
'''#lista de perguntas.
lista_perguntas = ['Telefonou para a vítima?',
                    'Esteve no local do crime?',
                    'Mora perto da vítima?',
                    'Devia para a vítima?',
                    'Já trabalhou com a vítima?']

#lista para armazenar as respostas
lista_respostas = []

# contador  
cont = 0          

#fazer as perguntas.
for c in range(len(lista_perguntas)):
    resp = input(f'{lista_perguntas[c]} SIM ou NÃO? ').upper()
    if resp == 'SIM' or resp == 'NAO':
      lista_respostas.append(resp)
      if resp  == 'SIM':
          cont += 1 # para cada indice da lista_resposta que for igual a sim contador soma +1
    else:
        print('Digite SIN ou NAO.')

         

print(f'Você respondeu "SIM" para {cont} perguntas')

# status
status = {2 : 'Suspeito(a)', 
          3 : 'Cúmplice',
          4 : 'Cúmplice',
          5 : 'Assassino'
          } 


print(status[cont])'''
    
#=========================================================================================
#Exer 3
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','.')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
        
lista = []
nota = 0
while nota != -1:
    nota = Validar_float('Digite uma nota: ')
    if nota >= 0:
        lista.append(nota)

media = sum(lista)/len(lista)
notas_maiores_que_media = [c for c in lista if c > media]
notas_menores_que_7 = [ m for m in lista if m < 7]

print(f'Foi digitado um total de {len(lista)} notas.')
print('Notas digitadas', *lista)
print('Notas na ordem inversa',*lista[::-1],sep='\n')
print(f'A soma de todas as médias é de {sum(lista)}')
print(f'A média das notas é de {media:.2f}')
print(f'Um total de {len(notas_maiores_que_media)} notas maior que a média')
print(f'Um total de {len(notas_menores_que_7)} notas menor que 7')
print('<<< OBRIGADO >>')'''
#==========================================================================================
#Ex5
'''def validar_float(msg):
    while True:
        v = input(f'{msg}: ')
        if ',' in v:
            v = v.replace(',', '.')
        try:
            v = float(v)
        except:
            print('Dado invalido.')
        else:
            return v
        
    
atletas = list()
dado_atletas = list()
lista_saltos = list()
while True:
    while True:
        nome = input('Atleta: ')
        if nome == '':
                break
        else:
            if nome.isalpha():
                atletas.append(nome)
                break
            else:
                print('O nome do atleta deve conter apena letras.')
    if nome == '':
        break
    for v in range(1,6):
        salto = validar_float(f'{v} salto: ')
        lista_saltos.append(salto)
        media = sum(lista_saltos)/len(lista_saltos)
        
    atletas.append(lista_saltos[:]) #adiciona uma copia raza da lista_saltos na lista atletas
    atletas.append(media) #adiciona a media na lista atletas
    lista_saltos.clear() # apaga a lista_saltos após ser adicionada na lista atletas 
    dado_atletas.append(atletas[:]) #adiciona os dados que forama dicionados na lista atletas
    atletas.clear() # em seguida apaga a lista atletas
    
# procurando os dados pelo indice
for v in dado_atletas:
    print('Nome:',v[0])
    print('Saltos:',*v[1],sep=' - ')
    print(f'Média dos saltos {v[2]:.2f}')
    print('='*30)'''
#===================================================================================================
#Ex17

'''votos = []
num = 1
print('<<< ENQUETE QUEM FOI O MELHOR JOGADOR >>>\n')
while num != 0:    
    
    num = int(input("Digite o número do jogador de 1 a 23 (para finalizar 0): "))
    if num > 23 or num < 0:
        print('Número inválido')
    else:
        if num > 0:
            votos.append(num)
            
tot = len(votos)
lista = []
for n in set(votos):
    c = votos.count(n)
    lista.append((c,n,f'{(c/tot*100):.1f}'))
lista.sort()
lista.reverse()
print('\n<<< Resultado da votação >>>')
print('='*30)
print(f'<<< Total de votos {tot} >>>')
print('='*30)
print(f'{"Jogador":<3}{"Votos":>8}{"%":>6}')
for vot,jog,per in lista:
    print(f'{jog:<3}{vot:>9}{per:>12}')'''
#============================================================================================
"""import os
lista_sistemas = [['Windows', 0],['Unix', 0],
['Linux', 0], ['Netware', 0],['Mac OS', 0], ['Outro', 0]]
total = []
opc = 1
while opc !=0:
    print('''1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro''')
    opc = int(input('Digite um número de 1 a 6 para votar ou 0 para finalizar: '))
    while opc > 6 or opc < 0:
        opc = int(input('Digite um número de 1 a 6 para votar ou 0 para finalizar: '))
    if opc != 0:
        total.append(opc)
        lista_sistemas[opc-1][1]+=1
    os.system('cls')

print(f'{"Sistema Operacional"}{"Votos":>8}{"%":>8}')
print(f'{"-"*19}{"-"*5:>8}{"-"*3:>9}')
l = []
for c in lista_sistemas:
    pecr = f'{(c[1] / len(total) * 100):.2f}'
    l.append([c[1],c[0],pecr])
    print(f'{c[0]}\t\t\t{c[1]}\t{pecr}')
print(f'{"-"*19}{"-"*5:>8}{"-"*3:>9}')
print(f'{"Total"}\t\t\t{len(total)}')
l.sort()
maior = max(l)
print(f'O Sistema Operacional mais votado foi o {maior[1]}, com {maior[0]} votos,correspondendo a {maior[2]} dos votos')"""
#-------------------------------------------------------------------------------------------------------
"""from time import sleep


def cabecalho(txt):
    print('='*45)
    print(txt.center(45))
    print('='*45)
    

salario = []
abono = []

cabecalho('<<< PROJEÇÃO DE GASTOR ABONO >>>')
sal = 1
while sal != 0:
    sal = float(input('Salario: '))
    if sal != 0:
        salario.append(sal)
cabecalho('<<< PROCESSANDO >>>')
sleep(1)

print('\nSalário\t\t  Abono')

for v in range(len(salario)):
    percentual = salario[v] * 0.20
    if percentual <= 100:
        percentual = 100
    print(f'R${salario[v]:>8.2f} \t R${percentual:>8.2f}')
    abono.append(percentual)


min = abono.count(100)

cabecalho(f'''
Foram processados {len(salario)} colaboradores
Total gasto com abonos: R$ {sum(abono):.2f}
Valor mínimo pago a {min} colaboradores
Maior valor de abono pago: R$ {max(abono):.2f}''')"""
#======================================================================================================
