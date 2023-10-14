num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou: {num}')
print(f'O número 9 aparaceu {num.count(9)} veze(s)')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')    
print(f'Os valores pares digitados foram: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end= '')