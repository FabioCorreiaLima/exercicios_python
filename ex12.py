produto = float(input('Digite o preço do produto? R$ '))
desconto = produto - (produto * 5/100)
print('Este produto de R${} com o desconto de 5% será R${} '.format(produto, desconto))