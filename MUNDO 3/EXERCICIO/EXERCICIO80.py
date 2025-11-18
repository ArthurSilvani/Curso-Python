#CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NÚMERICOS E CADASTRE-OS EM UMA LISTA, JA NA POSIÇÃO CORRETA DE INSERÇÃO
# NO FINAL, MOSTRE A LISTA ORDENADA NA TELA

import bisect

lista = list()

for cont in range(0,5):
    n = int(input('Digite um valor: '))
    bisect.insort(lista, n)
    print(f'O número {n} foi incluído na posição {lista.index(n)}!')
    

print(f'A ordem é {lista}!')



