
from random import randint# 1: Criar uma tupla com 10 números inteiros aleatórios e imprimir o maior e o menor número da tupla.
'''tupla_numeros = list(randint(1, 100) for c in range(10))
print(*tupla_numeros)
print(f'O maior valor da tupla é: {max(tupla_numeros)} e o menor é: {min(tupla_numeros)}')'''

# 2: Criar duas tuplas de números inteiros e mesclá-las em uma terceira tupla em ordem crescente.
'''tupla1 = (2, 5, 9, 12, 16)
tupla2 = (3, 6, 10, 15, 20)
tupla3 = tuple(sorted(tupla1 + tupla2))
print(tupla3)'''

# 3: Criar uma tupla com nomes de pessoas e ordená-la alfabeticamente.
'''tupla_nomes = ('Camila', 'Alcileia', 'Geovane', 'Fábio', 'Douglas', 'Alice', 'Antônia', 'Caio', 'Fernando')
tupla_ordenada = tuple(sorted(tupla_nomes))
print(*tupla_ordenada, sep=' , ')'''

# 4: Remover todas as ocorrências de um determinado número de uma tupla de números inteiros.
'''def validar_int(t,msg):
    while True:
        try:
            v = int(input(f'{msg}'))
        except:
            print('Valor invalido!')
        else:
           #6 : Criar uma lista com números inteiros e verificar se um determinado número está na tupla ou não.
            if v in t: # aqui verifica se esta na tupla ou não
                return v
            else:
                print('Não existe na tupla')
tupla_numeros = tuple(randint(1, 100) for c in range(10))
print(tupla_numeros)
res = validar_int(tupla_numeros, 'Informe o número que deseja remover da tupla: ')
#usando compreensssão de tupla para criar uma nova tupla
tupla_numeros = tuple(numero for numero in tupla_numeros if numero != res)
print(tupla_numeros)'''

# 5: Criar uma tupla com números inteiros e contar quantos números pares e quantos números ímpares existem na tupla.
'''tupla_numeros = tuple(randint(1, 100) for c in range(10))
pares = sum(1 for numero in tupla_numeros if numero % 2 == 0)
impares = sum(1 for numero in tupla_numeros if numero % 2 != 0)
print(tupla_numeros)
print(f'Números pares: {pares}\t\t Números ìmpares {impares}')'''

# 7: Criar uma tupla com nomes de frutas e verificar se uma determinada fruta está na tupla ou não.
tupla_frutas = ('abacate','amora','ameixa','acerola','abacaxi','açai','banana','carambola','caju',
'cereja','cacau','caqui','cupuaçu','damasco','figo','framboesa','graviola','goiaba','groselia',
'guarana','jaca','kiwi','laranja','limao')

#verificando se o nome é só letra
def is_alpha(msg):
    while True:
        try: 
            str_alpha = input(f'{msg}').lower()
            if str_alpha.isalpha():
                return str_alpha
        except:
            print('Informe somete letras.')
print(tupla_frutas)
print()
res = is_alpha('Digite o nome da fruta: ')
print('Existe na tupla.' if res in tupla_frutas else 'Não exite na lista.')

# 8: Criar uma tupla de números inteiros e calcular a soma de todos os números na tupla.
'''num = tuple(num for num in range(randint(2,101)))
print(num)
print(f'A soma de todos os números da tupla é de : {sum(num)}')'''

# 9: Criar uma tupla de números inteiros e calcular a média dos números na tupla.
'''num = tuple(num for num in range(randint(2,101)))
print(num)
print(f'A média de todos os números da tupla é de : {sum(num)/ len(num)}')'''

# 10: Criar uma tupla com nomes de pessoas e imprimir o primeiro e o último nome da tupla.
'''nomes = ("João Silva Pereira de Souza", "Maria Santos", "Pedro Alves", "Ana Paula Souza", "Luiz Felipe")
primeiro_ultimo = tuple((nome.split()[0],nome.split()[-1]) for nome in nomes)
print(*primeiro_ultimo)'''