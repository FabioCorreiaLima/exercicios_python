
#1: Criar uma lista com 10 números inteiros aleatórios e imprimir o maior e o menor número da lista.
from random import randint
'''lista_num = list(randint(1, 100) for c in range(10))
print(*lista_num)
print(f'O maior valor da lista é: {max(lista_num)} e o menor é: {min(lista_num)}')'''
#--------------------------------------------------------------------------------------------------
#2: Criar duas listas de números inteiros e mesclá-las em uma terceira lista em ordem crescente.
'''lista_1 = [3, 6, 7, 12, 15, -1, -5, 17]
lista_2 = [5, 7 , 9 , 3 , 2 , 54, 2, 6, 4, 0]

lista_2.extend(lista_1)
lista_2.sort()
print('Ordenando a lista', *lista_2, sep=' - ')'''
#--------------------------------------------------------------------------------------------------
#3: Criar uma lista com nomes de pessoas e ordená-la alfabeticamente.
'''lista_nomes = ['Camila', 'Alcileia', 'Geovane', 'Fábio', 'Douglas', 'Alice', 'Antônia', 'Caio', 'Fernando']
lista_nomes.sort()
print('Nomes em orden alfabetica', *lista_nomes, sep=' - ')'''
#--------------------------------------------------------------------------------------------------
#4: Remover todas as ocorrências de um determinado número de uma lista de números inteiros.
'''lista_num = list(randint(1, 100) for c in range(10))
def validar_int(lista,msg):
    while True:
        try:
            v = int(input(f'{msg}'))
        except:
            print('Valor invalido!')
        else:
           #6 : Criar uma lista com números inteiros e verificar se um determinado número está na lista ou não.
            if v in lista: # aqui verifica se esta na lista ou não
                return v
            else:
                print('Não existe na lista')

print('Aqui está uma lista de números',*lista_num, sep=' , ')
res = validar_int(lista_num, 'Informe o número que deseja remover da lista: ')
lista_num = [c for c in lista_num if c != res]
print(f'O número {res} foi removido da lista')
print(*lista_num, sep=' , ')'''




#------------------------------------------------------------------------------------------------
#5: Criar uma lista com números inteiros e contar quantos números pares e quantos números ímpares existem na lista.
'''cont_par = 0
cont_impar = 0
lista = [c for c in range(randint(2, 99))]
for c in lista:
    if c % 2 == 0:
        cont_par +=1
    else:
        cont_impar += 1
print(lista) 
print(f'A quantidade de números ímpares {cont_impar} e a quantidade de números pares {cont_par}')'''

#7 :Criar uma lista com nomes de frutas e verificar se uma determinada fruta está na lista ou não.
'''lista_frutas = ['abacate','amora','ameixa','acerola','abacaxi','açai','banana','carambola','caju',
'cereja','cacau','caqui','cupuaçu','damasco','figo','framboesa','graviola','goiaba','groselia',
'guarana','jaca','kiwi','laranja','limao']

#verificando se o nome é só letra
def is_alpha(msg):
    while True:
        try: 
            str_alpha = input(f'{msg}').lower()
            return str_alpha
        except:
            print('Informe somete letras.')
print(lista_frutas)
print()
res = is_alpha('Digite o nome da fruta: ')
print('Existe na lista.' if res in lista_frutas else 'Não exite na lista.')'''

#8: Criar uma lista de números inteiros e calcular a soma de todos os números na lista.
'''total_num = [num for num in range(randint(2,101))]
print(total_num)
print(f'A soma de todos os números da lista é de : {sum(total_num)}')'''

#9: Criar uma lista de números inteiros e calcular a média dos números na lista.
'''media_num = [num for num in range(randint(2,101))]
print(media_num)
print(f'A média de todos os números da lista é de : {sum(media_num)/ len(media_num)}')'''

#10: Criar uma lista com nomes de pessoas e imprimir o primeiro e o último nome da lista.
'''nomes = ["João Silva Pereira de Souza", "Maria Santos", "Pedro Alves", "Ana Paula Souza", "Luiz Felipe"]
primeiro_e_ultimo = [(nome.split()[0],nome.split()[-1]) for nome in nomes]
print(*primeiro_e_ultimo)'''

# #