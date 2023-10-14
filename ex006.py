# crie um algoritimo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada
n1 = float(input('Digite um numero: '))
#dobro=n1*2
#triplo=n1*3        # \n é para quebrar a linha .
#raiz=n1**(1/2)     # utiliza :.2f para quamdo tiver resultado com varias casas decimais ficar só a quantidade que voçê quiser .
print('O dobro de {} é igual a: {}: '.format(n1, n1*2))
print('O triplo de {} é igual a: {} \nA raiz quadrada de {} é igual a: {:.2f}'.format( n1, (n1*3),n1,pow(n1, (1/2))))