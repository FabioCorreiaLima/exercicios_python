from utilidades import moeda
from utilidades import dados
preco = dados.leiaDinheiro('Digite um valor:')
moeda.resumo(preco, 10, 20)