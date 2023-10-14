import moeda
preco = float(input('Digite um valor:'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'Aumentado 10%, temos R${moeda.aumentar(preco, 10)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'A metade de R${preco} é R${moeda.metade(preco)}')