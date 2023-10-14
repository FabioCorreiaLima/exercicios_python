
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura : '))
area =  larg * alt 
print(' Sua parede tem a dimensão de {}x{} e a área é de {}m².'.format( larg, alt ,area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))