def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except ( ValueError, TypeError):
            print('ERRO! Digite um número inteiro valido.')
            continue
        else:
            return(n)
        
num = leia_int('Digite um valor: ')
print(f'O valor digitado foi {num}')