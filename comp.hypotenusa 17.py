'''co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1-2)
print('A hipotenusa vai medir {} '.format(hi)) '''

from math import hypot
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {} '.format(hi))