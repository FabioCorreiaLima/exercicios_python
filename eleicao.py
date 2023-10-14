def linha():
    print('-='*30)
    
cand1 = cand2 = cand3 = cand4 = nulo = branco = 0

while True:
    linha()
    print('''
        [ 1 ] Candidato1
        [ 2 ] Candidato2
        [ 3 ] Candidato3
        [ 4 ] Candidato4
        [ 5 ] Branco
        [ 6 ] Nulo''')
    linha()
    while True:
        opcao = str(input('Digite o número do candidato: ')).upper().strip()
        if opcao == 'FIM':
            break
        elif '1' <= opcao <= '6':
            break
        print('ERROR! ', end='')
    if opcao == '1':
        cand1 += 1
    else:
        if opcao == '2':
            cand2+=1
        elif opcao == '3':
            cand3+=1

        elif opcao == '4':
            cand4 +=1
            
        elif opcao == '5':
            
            branco +=1
        else:
            nulo += 1
    if opcao == 'FIM':
        break
print(f'Total de votos do candidato1 {cand1}')
print(f'Total de votos do candidato2 {cand2}')
print(f'Total de votos do candidato3 {cand3}')
print(f'Total de votos do candidato4 {cand4}')
print(f'Total de votos Nulo {nulo}')
print(f'Total de votos Branco {branco}')   
