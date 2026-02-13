
msg = ('     RESUMO DO VALOR     ')

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

def resumo(n=0, taxa=0, taxar=0):

    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))  
   
    print(f'Metade:     \tR${metade(n, True)}')
    print(F'Dobro:      \tR${dobro(n,True)}')
    print(f'Aumenta:    \tR${aumentar(n, taxa, True)}')
    print(f'Diminui:    \tR${diminuir(n, taxar, True)}')

    print('-'*20)