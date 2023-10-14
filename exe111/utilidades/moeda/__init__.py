def aumentar(preco = 0, taxa = 0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else Moeda(res)


def diminuir(preco = 0, taxa = 0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else Moeda(res)

    
def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if formato is False else Moeda(res)

    
def metade(preco= 0, formato=False):
    res = preco / 2
    return res if formato is False else Moeda(res)
    
    
def Moeda(preco, moeda='R$'):
    return f'{moeda} {preco:.0f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('=-'*30)
    print('Resumo do valor '.center(30))
    print('=-'*30)
    print(f'Preço analisado: \t{Moeda(preco)}')
    print('=-'*30)
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'A metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa} de redução: \t\t{diminuir(preco, True)}')
    print(f'{taxar} de aumento: \t\t{aumentar(preco, True)}')
    print('=-'*30)