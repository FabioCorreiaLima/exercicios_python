lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite {c}ª número: ')))

print(f'Voce digitou os valores {lista}')

print(f'O maior valor digitado foi: {max(lista)} na(s) posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...',end='' )
print(f'\nO menor valor digitado foi: {min(lista)} na(s) posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
        