def linha():
    print('-'*40)
listagem = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.00,
            'Estojo', 8.00,
            'Transferidor', 5.00,
            'Compasso', 10.00,
            'Mochila', 100.00,
            'Canetas', 22.00,
            'Livros', 34.90)

linha()
print(f'{"LISTAGEM DE PREÇOS":^40}')
linha()
for lista in listagem:
    if type(lista) is str:
         print(f'{lista:.<30}', end='')
    else:
          print(f'R$ {lista:>7.2f}')
linha()