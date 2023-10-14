def linha():
    print('-='*20)

times = ('Corrintians', 'Flamengo', 'Fluminense', 'Atletico-MG','Bota Fogo','São Paulo', 
         'Vasco', 'Palmeiras','Ponte Preta','Cruzeiro', 'Goiais','Atletico-GO')

linha()
print('  LISTA DE TIMES BRASILEIRÃO  ')
linha()
for c in times:
    print(c)
linha()
print(f'''Os 5 primeiros times são : {times[0:5]}
-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=--=-=--=-=-=---==-=-=-=-=-==--
Os 4 ultimos times são: {times[-4:]}
Lista em ordem alfabetica {sorted(times)}''')
