def metade(n, format=False):
    res = n / 2
    return res if format is False else moeda(res)

def dobro(n, format=False):
    res = n * 2
    return res if format is False else moeda(res)

def aumentar(n, taxa, format=False):
    res = n + ( n * taxa / 100)
    return res if format is False else moeda(res)

def diminuir(n, taxa, format=False):
    res = n - ( n * taxa / 100)
    return res if format is False else moeda(res)

def moeda(n):
    return f'R${n:.2f}'.replace('.',',')