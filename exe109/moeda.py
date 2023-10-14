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