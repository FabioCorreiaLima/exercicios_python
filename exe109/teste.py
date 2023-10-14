import moeda
preco = float(input('Digite um valor:'))
print(f'A metade de {moeda.Moeda(preco)} é {moeda.metade(preco, True)}')
print(f'Aumentado 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'O dobro de {moeda.Moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.Moeda(preco)} é {moeda.metade(preco, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')