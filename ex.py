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


cand = [['1', 0],['2', 0], ['3', 0], ['4', 0], ['5', 0], ['6', 0], ['7', 0], ['8', 0], ['9', 0],
['10', 0], ['11', 0], ['12', 0], ['13', 0], ['14', 0], ['15', 0], ['16', 0], ['17', 0], ['18', 0],
['19', 0], ['20', 0], ['21', 0], ['22', 0], ['23', 0]]

votos = []
num = 1

while num != 0:    
    num = int(input("Digite o número do jogador de 1 a 23 (para finalizar 0): "))
    if num > 23 or num < 0:
        print('Número inválido')
    else:
        if num > 0:
            votos.append(num)
            cand[num-1][1]+=1
print('='*30)
print(f'Total de votos {len(votos)}')
print('='*30)
print(f'{"Jogador":<3}{"Votos":>8}{"%":>8}')
for c in cand:
    if c[1]!=0:
        f = c[1] / len(votos)*100
        print(f'{c[0]:<2}{c[1]:>10}       {f:.2f}')




