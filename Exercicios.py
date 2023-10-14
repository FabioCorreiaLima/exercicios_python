#Ex1
'''while True:
    try:
        n1 = float(input('Digite um número: '))
    except:
        print('Digite um número Valido.')
    else:
        print(f'O número informado foi {n1:.2f}')
        break'''
#----------------------------------------------------------------------------
#Ex2
'''while True:
    try:
        n1 = float(input('Digite 1ª número: '))
        n2 = float(input('Digite 2ª número: '))
        s = n1+n2
    except:
        print('Valores invalidos')
    else:
        print(f'A soma de {n1} + {n2} = {s:.2f}')
        break
    '''
#----------------------------------------------------------------------------
#Ex3
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
cont = 0
lista = []
print('MÉDIA DAS NOTAS BIMESTRAIS')

for c in range(1,5):
    n1 = Validar_float(f'{c}ª nota: ')
    lista.append(n1)
    cont+=1
print(f'A média é {sum(lista)/cont:.2f}')'''

#-----------------------------------------------------------------------------
#Ex4
'''print('TRANSFORMANDO METROS PARA CENTIMETOS')
while True:
    try:
        m = float(input('Metragem? '))
        c = m * 100
    except:
        print('Valor invalido')
    else:
        print(f'{m:.2f} metro(s) equivale a {c:.2f} centimetro(s)')
        break'''
#-----------------------------------------------------------------------------
#Ex5
'''pi = 3.14
print('ÀREA DA CIRCUNFERÊNCIA')
while True:
    try:
        raio = float(input('Digite o raio da circunferencia: '))
        area = pi * raio**2
    except:
        print('Valor invalido')
    else:
        print(f'A àrea da circunferência é de {area:.2f}m²')
        break'''
#----------------------------------------------------------------------------
#Ex6
'''print('CALCULANDO A ÀREA DE UM QUADRADO EM (m²)')
while True:
    try:
        L = float(input('Digite a largura do quadrado: '))
        area = L**2
    except:
        print('Valor invalido')
    else:
        print(f'A àrea do quadrado é de {area:.2f}m²\nO dobro dessa àrea é de {area*2:.2f}m²')
        break'''
#-----------------------------------------------------------------------------------------
#Ex7
'''while True:
    sexo = input('Infome seu sexo [F/M]: ').upper().strip()
    if sexo in 'MF':
        print('Sexo validado')
        break
    else:
        print('ERRO! Digite [F]-feminino [M]-masculino')'''
#------------------------------------------------------------------------------------------
#Ex8
'''print('VERIFICANDO SE UMA LETRA É CONSOANTE OU VOGAL')
while True:
    letra = input("Informe uma letra:").strip().lower()
    if letra.isalpha():
        if letra in 'aeiou':
            print('É vogal')
            break
        else:
            print('É consoante')
            break
    else:
        print('Digite apenas letra.')'''
#------------------------------------------------------------------------------------------
#Ex9
from hashlib import new
import os 

'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
        

while True:
    print('CALCULANDO MÉDIA DE UM ALUNO')
    nota1 = Validar_float('1ª nota: ')
    nota2 = Validar_float('2ª nota: ')
    media = (nota1 + nota2) / 2
    if media >= 7:
        print(f'Sua média é de {media} <<<Aprovado.>>>')
        
    elif media < 5:
        print(f'Sua média é de {media} <<<Reprovado.>>>')
        
    else:
        print(f'Sua média é de {media} <<<Recuperação.>>>')
    while True:
        res = input('Quer continuar? [S/N]: ').upper().strip()
        if res in 'SN':
            break
        else:
            print('Digite [S]-Sim ou [N]-Não.')
    if res == 'N':
        break    
    elif res == 'S':
        os.system('cls')
print('<<< OBRIGADO >>>')'''
        
#-----------------------------------------------------------------------------
#Ex10
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','.')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
        
lista = []


for c in range(1,4):
    numeros = Validar_float(f'{c}ª Número: ')
    lista.append(numeros)

print(f'Os números digitados foram {lista}',
f'\nO maior valor digitado foi {max(lista)}')'''
    #------------------------------------------------------------------------------
#Ex11
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
        
lista = []


for c in range(1,4):
    numeros = Validar_float(f'{c}ª Número: ')
    lista.append(numeros)

print('Digite apenas números')

print(f'O maior valor digitado foi {max(lista)}\nE o menor foi {min(lista)}')'''

#--------------------------------------------------------------------------------------
#Ex12
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
lista = []

for c in range(1,4):
    produtos = Validar_float(f'{c}ª Valor do produto R$:')
    lista.append(produtos)
print(f'Você deve comprar o produto mais barato de R$:{min(lista)}')'''

#--------------------------------------------------------------------------------------
#Ex13
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
        
lista = []

for c in range(1,4):
    numeros = Validar_float(f'{c}ª Número: ')
    lista.append(numeros)

print(f'Os números digitados em ordem decrescente: {sorted(lista, reverse= True)}')'''

#---------------------------------------------------------------------------------------------
#Ex14
'''print('<<< VALIDANDO TURNOS >>>')
while True:
    turno = input('Infome seu Turno [M/V/N]: ').upper().strip()
    if turno in 'MVN':
        if turno == 'M':
            print('<<BOM DIA!>>')
            break
        elif turno == 'V':
            print('<<BOA TARDE!>>')
            break
        else:
            print('<<BOA NOITE>>')
            break
    else:
        print('ERRO! Digite [M]-Matutino [V]- Vespertino [N]- Noturno')'''
#----------------------------------------------------------------------------------------------
#Ex15
'''def linha():
    print('='*20)
    
salario_atual = 1
while salario_atual > 0:
    linha()
    print('REAJUSTE SALARIAL')
    linha()
    try:
        salario_atual = float(input('Informe salário atual ou [0] para finalizar: R$'))
    except ValueError:
        print('Informação invalida')
        linha()
    else:
        pass
    if salario_atual == 0:
        break
    elif salario_atual <= 280:
        novo_salario = salario_atual + (salario_atual * 20 / 100)
        linha()
        print(f'O novo salário com um reajuste de 20% será de {novo_salario:.2f} ')
        linha()
    elif 700 >= salario_atual > 280:
        novo_salario = salario_atual +(salario_atual * 15 / 100)
        linha()
        print(f'O novo salário com um reajuste de 15% será de {novo_salario:.2f} ')
        linha()
    elif 1500 > salario_atual > 700:
        novo_salario = salario_atual + (salario_atual * 10 / 100)
        linha()
        print(f'O novo salário com um reajuste de 10% será de {novo_salario:.2f} ')
        linha()
    else:
        novo_salario = salario_atual + (salario_atual * 5 / 100)
        print(f'O novo salário com um reajuste de 5% será de {novo_salario:.2f} ')
print('<<<Programa finalizado>>>')'''
#---------------------------------------------------------------------------------------------------------
#Ex16
'''import os

def linha():
    print('='*40)
    
    
def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            linha()
            print('\nValor invalido! Digite apenas números')
            linha()
        else:
            return validar
        

def cabecalho(msg):
    tam = len(msg)+4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    


# Programa principal
while True:
    cabecalho('FOLHA DE PAGAMENTO')
    V_H = Validar_float('Informe quanto você recebe por hora: R$')
    H_T = Validar_float('Infome quantidade de horas trabalhadas no mês: ')
    salario_bruto = V_H * H_T
    if salario_bruto > 0 and salario_bruto <= 900:
        ir = 0.0
    elif 1500 > salario_bruto > 900:
        ir = 5
    elif salario_bruto <= 2500:
        ir = 10
    else:
        ir = 20

    IR = salario_bruto * (ir / 100)
    INSS = salario_bruto * (10 / 100)
    FGTS = salario_bruto * (11 / 100)
    total_de_descontos = IR + INSS
    salario_liquido = salario_bruto - total_de_descontos
    linha()
    print(f'\nSalário Bruto     : R${salario_bruto:.2f}'
          f'\n(-) IR ({ir}%)      : R${IR:.2f}'
          f'\n(-) INSS ( 10%)   : R${INSS:.2f}'
          f'\nFGTS (11%)        : R${FGTS:.2f}'
          f'\nTotal de descontos: R${total_de_descontos:.2f}'
          f'\nSalário Liquido   : R${salario_liquido:.2f}')
    linha()
    while True:
        res = input('Quer continuar? [S/N]: ').upper().strip()
        if res in 'SN':
            if res == 'N':
                break
            elif res == 'S':
                os.system('cls')
                break
        else:
            print('Digite [S]-Sim ou [N]-Não.')
    if res == 'N':
        break
print('<<OBRIGADO>>')'''
#---------------------------------------------------------------------------------------------------
#Ex17
        
# Programa principal

'''print('<< VALIDANDO INFORMAÇÕES >>')

while True:
    nome = input('Infome seu nome: ').upper().strip()
    if not nome.isalpha():
        print('Digite apenas letras.')
    else:
        if len(nome)>3:
            break
        else:
            print('O nome deve ter mais de 3 caracters.')
while True:
    try:
        idade = int(input('Informe sua idade: '))
    except:
        print('Valor invalido')
    else:
        if 150 >= idade > 0:
            break
        else:
            print('Digite uma idade menor que 150 e maior que 0.')
while True:
    try:
        salario = float(input('Informe o sálario: R$'))
    except:
        print('Valor invalido')
    else:
        if salario > 0:
            break
        else:
            print('Salaria tem que ser maior que 0.')
while True:
    sexo = input('Informe seu sexo [F/M]: ').upper().strip()
    if sexo in 'FM':
        break
    else:
        print('Digite [F]-Feminino ou [M]-Masculino.')
while True:
    estado_civil = input('Informe seu estado civil [S/C/V/D]: ').upper().strip()
    if estado_civil in 'SCVD':
        break
    else:
        print('Digite [S]-Solteiro(a), [C]-Casado(a), [V]-Viuvo(a), [D]-Divorciado(a).')
    
print('<<<Dados validados>>>')'''
#----------------------------------------------------------------------------------------------
#Ex18
'''populacao_A = 80000
populacao_B = 200000
anos = 0
while populacao_A < populacao_B:
    populacao_A += (populacao_A * 3/100)
    populacao_B += (populacao_B * 1.5/100)
    anos += 1 
print(f'Em {anos-1} anos a população (A) com taxa de 3% igulará com a população (B).',
      f'\nEm {anos} anos a populção (A) com taxa de 3% ultrapassará a população (B).')'''
#-----------------------------------------------------------------------------------------------
#Ex19
'''import os


def Validar_float(msg):
    while True:
        
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
            print(validar)
        try:
            validar = float(validar)
        except:
            print('Digite apenas valores númericos.')
        else:
            return validar



while True:
    print('<<< CRESCIMENTO POPULACIONAL >>>')
    anos = 0
    populacao_A = Validar_float('Informe o número de habitantes do pais (A): ')
    taxa_A = Validar_float('Informe a taxa de crescimento da popupação (A): ')
    populacao_B = Validar_float('Informe o número de habitantes do pais (B): ')
    taxa_B = Validar_float('Informe a taxa de crescimento da popupação (B): ')
    while populacao_A < populacao_B :
        
        populacao_A += (populacao_A * taxa_A)
        populacao_B += (populacao_B * taxa_B)
        anos += 1 
    print(f'\nEm {anos} anos a populção (A) com taxa de {taxa_A}% ultrapassará a população (B).')
    res = input('Quer continuar? [S/N]: ').upper().strip()
    if res in 'SN':
        if res == 'N':
            break
        elif res == 'S':
            os.system('cls')
            continue
    else:
        print('Digite [S]-Sim ou [N]-Não.')
    
print('<<< OBRIGADO >>>')'''
#-------------------------------------------------------------------------------------------
#Ex20
'''for c in range(21):
    print(c)
    
print('<< A seguir os número de cima um ao lado do outro >>')
for c in range(21):
    print(c, end='<-')'''
#-------------------------------------------------------------------------------------------
#Ex21
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
        
lista = []


for c in range(1,6):
    numeros = Validar_float(f'{c}ª Número: ')
    lista.append(numeros)

print('Digite apenas números')

print(f'Os números digitados foram {lista}.',
    f'\nO maior valor digitado foi {max(lista)}')'''
#----------------------------------------------------------------------------------------
#Ex22
'''def Validar_float(msg):
    while True:
        validar = input(f'{msg}')
        if ',' in validar:
            validar = validar.replace(',','')
        try:
            validar = float(validar)
        except:
            
            print('\nValor invalido! Digite apenas números')
            
        else:
            return validar
        
lista = []
cont = 0

for c in range(1,6):
    numeros = Validar_float(f'{c}ª Número: ')
    lista.append(numeros)
    cont += 1 

print('Digite apenas números')

print(f'Os números digitados foram {lista}.',
    f'\nA média dos valores digitados é {sum(lista)/cont}')'''
#------------------------------------------------------------------------------------------------
#Ex23
'''for c in range(2,50):
    if c % 2 == 0:
        pass
    else:
        print(c, end='<-')'''
#------------------------------------------------------------------------------------------------
#Ex24
'''def Validar_int(msg):
    while True:
        validar = input(f'{msg}')
        try:
            validar = int(validar)
        except:
            
            print('\nValor invalido! Digite apenas número inteiro.')
            
        else:
            return validar
def intervalo(i, f): #parametros [i] inicio, [f] fim
    print(f'Os números inteiros no intervalo de {i} e {f} são ',end='')
    for a in range(i+1, f):
        print(a, end='<-')
    
        
n1 = Validar_int('Informer um número inteiro: ')
n2 = Validar_int('Informer outro número inteiro: ')

if n1 > n2:
    intervalo(n2, n1)
    
elif n1 < n2:
    intervalo(n1, n2)
     
else:
    print('Os numeros são iguais.')'''

#