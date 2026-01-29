#CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATORIOS
#GUARDE ESSES RESULTADOS EM UM DICIONARIO. NO FINAL, COLOQUE ESSE DICIONARIO EM ORDEM
#SABENDO QUE O VENCEDOR TIROU MAIOR NÚMERO NO DADO

from random import randint
import time
from operator import itemgetter
dado = { 'jogador1': randint(1,6), 
        'jogador2': randint(1, 6), 
        'jogador3': randint(1, 6), 
        'jogador4': randint(1, 6)}
ranking = list()

print('\033[0;34;40mValores do Sorteio:\033[0;0;0m')
for k, v in dado.items():
    print(f'O {k} tirou o número {v}!') 
    time.sleep(1)
  
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True) #A função itemgetter no Python, encontrada no módulo operator, serve para recuperar um ou mais itens de uma estrutura de dados (como listas, tuplas ou dicionários) com base em um índice ou chave específica. 
print('-'*10)
print(' == RANKING DO SORTEIO ==    ')

for k, v in enumerate(ranking):
    print(f' {k+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)