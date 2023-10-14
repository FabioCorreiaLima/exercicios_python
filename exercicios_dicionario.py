# 1: Crie um dicionário com informações pessoais:
dados_pessoal = {'nome': 'João', 'idade': 25, 'endereco': 'Estrada Duas Àguas', 'telefone': '(11) 97249-7589'}

# 2: Adicionar um item a um dicionário existente:
dados_pessoal['email'] = 'camila.carvalho@gmail.com'

# 3: Remover um item de um dicionário existente:
del dados_pessoal['telefone']

# 4: Atualizar o valor de um atributo em um dicionário existente:
dados_pessoal['endereco'] = 'Rua São João Batista'

# 5: Contar o número de itens em um dicionário:
num_itens = len(dados_pessoal)
print(num_itens)

# 6: Verifique se um determinado atributo está presente em um dicionário:
if 'idade' in dados_pessoal:
    print('O atributo idade está presente no dicionário.')
    
# 7: Obtenha o valor de um determinado atributo em um dicionário:
idade = dados_pessoal['idade']

# 8: Percorrer todos os itens em um dicionário e imprimir os atributos e valores:
for k, v in dados_pessoal.items():
    print(f'{k} \t\t\t {v}')
    
# 9: Agrupar informações relacionadas em um único dicionário:
pessoas = {'João': {'idade': 25, 'endereço': 'Estrada Barriguda', 'telefone': '(21) 98457-9139'},
           'Maria': {'idade': 30, 'endereço': 'Rua dos Pinheiros', 'telefone': '(44) 94858-4588'}}

# 10: Armazenar uma contagem de palavras em um texto usando um dicionário:
texto = "Armazenar uma contagem de palavras em um texto usando um dicionário"
contagem_palavras = {palavra: texto.split().count(palavra) for palavra in set(texto.split())}
print(contagem_palavras)
