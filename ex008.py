# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
medida = float(input('Uma distancia em metros: '))
cm = medida*100
mlm = medida*1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mlm))