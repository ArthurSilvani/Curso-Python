def lin():
    print('-' * 30)

lin()
print('     CURSO TOP       ')
lin()

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

titulo('    AULA 20     ')


def soma(a, b):
    print(F' A = {a} B = {b}!')
    s = a + b
    print(F'A soma de A + B = {s}!')

soma(9,0)
soma(3,5)
soma(1,5)

#EMPACOTAMENTOS
def  contador(*num):
    print(num)

contador(4, 7, 2, 7)
contador(2, 6, 4)
contador(1)

#USANDO LISTA
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
dados = [ 1, 2, 2, 6, 8]

dobra(dados)

print(dados)