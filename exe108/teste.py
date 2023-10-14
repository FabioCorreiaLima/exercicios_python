import moeda
preco = float(input('Digite um valor:'))
print(f'A metade de {moeda.Moeda(preco)} é {moeda.Moeda(moeda.metade(preco))}')
print(f'Aumentado 10%, temos {moeda.Moeda(moeda.aumentar(preco, 10))}')
print(f'O dobro de {moeda.Moeda(preco)} é {moeda.Moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.Moeda(preco)} é {moeda.Moeda(moeda.metade(preco))}')