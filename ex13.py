salabruto = float(input('Informe o salario: R$ '))
aumento = salabruto + (salabruto * 15/100)
print('Este salario de R${} com aumento de 15% será R${:.3f} '.format(salabruto, aumento))