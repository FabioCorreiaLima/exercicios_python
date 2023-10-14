#  crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos Dólares ela pode comprar.
real = float(input(' Digite quanto dinheiro você tem? R$: '))
dolar = real / 5.27
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))