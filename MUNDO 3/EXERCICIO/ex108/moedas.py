def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumentar(n, taxa):
    res = n + ( n * taxa / 100)
    return res

def diminuir(n, taxa):
    res = n - ( n * taxa / 100)
    return res

def moeda(format):
    return f'R${format:.2f}'.replace('.',',')