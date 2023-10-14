def linha():
    print('=-'*30)

clientes = []
for c in range(0, 3):
    nome = str(input('Nome do cliente: ')).upper().strip()
    compras = float(input('Compras do ano passado: R$'))
    clientes.append(nome)
    clientes.append(compras)
linha()
for l in clientes:
    if type(l) is str:
        print(f'{l:.<30}', end='')
    else:
        print(f'{l:>7}')
linha()