#CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA.
# DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA

from random import randint

tupla0 = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)) 

gerador = ( tupla0)

print(f' Os valores sorteados foram: {gerador}')

print(f'O maior valor é {max(tupla0)}.')
print(f'O menor valor é {min(tupla0)}.')
