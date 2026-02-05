#faça um programa que tenha uma lista chamada números e duas funçoes chamadas sorteria() e somaPar()
#A primeira função vai sortear 5 num e vai colocar-lós dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores Pares sorteados pela função anterior

import random
from time import sleep

números = list()
par = list()

def sorteia():
    valores = random.sample(range(1,60), 5)
    números.extend(valores)
    print(f'Sorteando 5 valores da lista: {valores}')

def somaPar():
    soma = 0
    for n in números:
        if n % 2 == 0:
            par.append(n)
            soma += n
    print(f'Números pares: {par}')
    print(f'Soma dos pares: {soma}')

sorteia() 
somaPar()