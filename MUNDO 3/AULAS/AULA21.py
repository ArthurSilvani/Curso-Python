help(print) #FUNÇÃO QUE AJUDA A ENTENDER OUTRAS FUNÇÕES.

#-------------------------------------------------------------------------------------------

def contador(i, f, p): #DOCSTRINGS
    """
    Contador teste
    
    :param i: inicio
    :param f: fim
    :param p: pula

    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')

help(contador)
contador(0, 100, 10)

#-------------------------------------------------------------------------------------------

def somar(a, b, c=0): #PARAMETROS OPCIONAIS, POR COM QUE UM DOS PARAMETROS SEJA IGUAL A SUA NECESSIDADE.
    s = a + b + c
    print(f'A soma dos valores é {s}.')

somar(7, 8, 4)
somar(6, 7)

#-------------------------------------------------------------------------------------------
def funçao(): #ESCOPO GLOBAL E LOCAL 
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funçao()
print(f'N1 fora vale {n1}')

#--------------------------------------------------------------------------------------------

def teste(b):
    global a # ao utlizar esse comando estou transformando todos os A's em valor 8
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

#--------------------------------------------------------------------------------------------
def cont(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = cont(2, 3, 5)
r2 = cont(9, 5, 8)
print(f'Os resultados sao {r1}, {r2}')
