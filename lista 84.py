lista = []
princ = []
maior = menor = 0
while True:
    lista.append(input('Digite seu nome: ').upper().strip())
    lista.append(float(input('Informe seu peso: ')))
    princ.append(lista[:])
    lista.clear()
    resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if resp == 'N':
        break
print(f'Foram cadastrada {len(princ)}')
print(f'O maior peso foi de {max(princ)}', end='')
for c in princ:
    if c[1] == max(princ):
        print(f'[{c[0]}]', end='')
print()
print(f'O menor peso foi de {min(princ)}', end='')
for c in princ:
    if c[1] == min(princ):
        print(f'[{c[0]}]', end='')
        
    
    